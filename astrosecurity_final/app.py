import os
import random
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template,
                   request, url_for)
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from data.preguntas_facil import preguntas_facil
from data.preguntas_intermedio import preguntas_intermedio
from data.preguntas_avanzado import preguntas_avanzado

load_dotenv()

# ── Aplicación ────────────────────────────────────────────────────────────────

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///astrosecurity.db')
# Render entrega postgres:// pero SQLAlchemy necesita postgresql://
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'astrosecurity_dev_key_xK9#mP2')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'presentacion'

# ── Modelos ───────────────────────────────────────────────────────────────────

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id            = db.Column(db.Integer, primary_key=True)
    nombre        = db.Column(db.String(120), nullable=False)
    correo        = db.Column(db.String(254), unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    preocupacion  = db.Column(db.Text, default='')
    creado_en     = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Progreso de niveles normales (nombre del nivel desbloqueado más alto)
    nivel_desbloqueado = db.Column(db.String(20), default='facil')

    # Mejor puntaje por nivel (para desbloquear examen)
    mejor_pct_facil      = db.Column(db.Integer, default=0)
    mejor_pct_intermedio = db.Column(db.Integer, default=0)
    mejor_pct_avanzado   = db.Column(db.Integer, default=0)

    # Exámenes desbloqueados
    examen_facil_desbloqueado      = db.Column(db.Boolean, default=False)
    examen_intermedio_desbloqueado = db.Column(db.Boolean, default=False)
    examen_avanzado_desbloqueado   = db.Column(db.Boolean, default=False)

    historial = db.relationship('Historial', backref='usuario', lazy=True,
                                order_by='Historial.fecha.desc()')

    # Flask-Login
    @property
    def is_active(self):      return True
    @property
    def is_authenticated(self): return True
    @property
    def is_anonymous(self):   return False
    def get_id(self):         return str(self.id)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

    def mejor_pct(self, nivel):
        return getattr(self, f'mejor_pct_{nivel}', 0)

    def examen_desbloqueado(self, nivel):
        return getattr(self, f'examen_{nivel}_desbloqueado', False)

    def actualizar_mejor_pct(self, nivel, pct):
        attr = f'mejor_pct_{nivel}'
        if pct > getattr(self, attr, 0):
            setattr(self, attr, pct)
        # Desbloquear examen si supera 60%
        if pct >= 60:
            setattr(self, f'examen_{nivel}_desbloqueado', True)


class Historial(db.Model):
    __tablename__ = 'historial'

    id       = db.Column(db.Integer, primary_key=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha    = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    nivel    = db.Column(db.String(30), nullable=False)   # 'Facil', 'Examen Facil', etc.
    aciertos = db.Column(db.Integer, nullable=False)
    total    = db.Column(db.Integer, nullable=False)
    pct      = db.Column(db.Integer, nullable=False)
    aprobado = db.Column(db.Boolean, nullable=False)


@login_manager.user_loader
def load_user(uid):
    return db.session.get(Usuario, int(uid))


# ── Datos de preguntas ────────────────────────────────────────────────────────

BANCO = {
    'facil':      preguntas_facil,
    'intermedio': preguntas_intermedio,
    'avanzado':   preguntas_avanzado,
}

ORDEN_NIVELES   = ['facil', 'intermedio', 'avanzado']
PREGUNTAS_QUIZ  = 10
PREGUNTAS_EXAMEN = 40
PCT_APROBAR_NIVEL  = 80   # % para desbloquear siguiente nivel
PCT_APROBAR_EXAMEN = 60   # % mínimo para desbloquear examen (sobre nivel correspondiente)

# ── Helpers ───────────────────────────────────────────────────────────────────

def _nivel_idx(nivel):
    return ORDEN_NIVELES.index(nivel) if nivel in ORDEN_NIVELES else 0


def _nivel_desbloqueado_idx():
    return _nivel_idx(current_user.nivel_desbloqueado)


def _construir_quiz(nivel, cantidad):
    seleccion = random.sample(BANCO[nivel], min(cantidad, len(BANCO[nivel])))
    out = []
    for p in seleccion:
        opciones = p['opciones'][:]
        random.shuffle(opciones)
        out.append({'pregunta': p['pregunta'], 'opciones': opciones, 'correcta': p['correcta']})
    return out


# ── Inicialización de la base de datos ───────────────────────────────────────

with app.app_context():
    db.create_all()


# ── Rutas de autenticación ────────────────────────────────────────────────────

@app.route('/')
def bienvenida():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))
    return render_template('bienvenida.html')


@app.route('/presentacion')
def presentacion():
    return render_template('presentacion.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))
    error = None
    if request.method == 'POST':
        nombre       = request.form.get('nombre', '').strip()
        correo       = request.form.get('correo', '').strip().lower()
        password     = request.form.get('password', '')
        preocupacion = request.form.get('preocupacion', '').strip()

        if not nombre or not correo or not password:
            error = 'Todos los campos son obligatorios.'
        elif len(password) < 6:
            error = 'La contraseña debe tener al menos 6 caracteres.'
        elif Usuario.query.filter_by(correo=correo).first():
            error = 'Ya existe una cuenta con ese correo.'
        else:
            u = Usuario(nombre=nombre, correo=correo, preocupacion=preocupacion)
            u.set_password(password)
            db.session.add(u)
            db.session.commit()
            login_user(u, remember=True)
            return redirect(url_for('inicio'))

    return render_template('registro.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))
    error = None
    if request.method == 'POST':
        correo   = request.form.get('correo', '').strip().lower()
        password = request.form.get('password', '')
        u = Usuario.query.filter_by(correo=correo).first()
        if u and u.check_password(password):
            login_user(u, remember=True)
            return redirect(request.form.get('next') or url_for('inicio'))
        error = 'Correo o contraseña incorrectos.'
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('bienvenida'))


# ── Rutas principales ─────────────────────────────────────────────────────────

@app.route('/inicio')
@login_required
def inicio():
    return render_template('index.html')


@app.route('/perfil', methods=['POST'])
@login_required
def perfil():
    current_user.nombre       = request.form.get('nombre', '').strip() or current_user.nombre
    current_user.correo       = request.form.get('correo', '').strip().lower() or current_user.correo
    current_user.preocupacion = request.form.get('preocupacion', '').strip()
    nueva_pw = request.form.get('nueva_password', '').strip()
    if nueva_pw:
        if len(nueva_pw) < 6:
            flash('La nueva contraseña debe tener al menos 6 caracteres.', 'error')
            return redirect(url_for('inicio'))
        current_user.set_password(nueva_pw)
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route('/historial')
@login_required
def historial():
    registros = Historial.query.filter_by(user_id=current_user.id)\
                               .order_by(Historial.fecha.desc()).all()
    return render_template('historial.html', registros=registros)


@app.route('/objetivo')
@login_required
def objetivo():
    return render_template('objetivo.html')


@app.route('/retroalimentacion')
@login_required
def retroalimentacion():
    return render_template('retroalimentacion.html')


@app.route('/soporte')
@login_required
def soporte():
    return render_template('soporte.html')


# ── Niveles ───────────────────────────────────────────────────────────────────

@app.route('/niveles')
@login_required
def niveles():
    return render_template('niveles.html',
                           nivel=current_user.nivel_desbloqueado,
                           usuario=current_user)


# ── Quiz normal (10 preguntas) ────────────────────────────────────────────────

@app.route('/quiz/<nivel>')
@login_required
def verificar_acceso(nivel):
    if nivel not in BANCO:
        return redirect(url_for('niveles'))
    if _nivel_idx(nivel) > _nivel_desbloqueado_idx():
        return redirect(url_for('niveles'))

    preguntas = _construir_quiz(nivel, PREGUNTAS_QUIZ)
    # Guardar en sesión del servidor Flask (no en la cookie del cliente)
    import flask
    flask.session['preguntas_actuales'] = preguntas
    flask.session['nivel_actual']       = nivel
    flask.session['modo_examen']        = False
    return render_template('quiz.html', preguntas=preguntas, nivel=nivel, es_examen=False)


# ── Examen (40 preguntas) ─────────────────────────────────────────────────────

@app.route('/examen/<nivel>')
@login_required
def examen(nivel):
    if nivel not in BANCO:
        return redirect(url_for('niveles'))
    if not current_user.examen_desbloqueado(nivel):
        return redirect(url_for('niveles'))

    preguntas = _construir_quiz(nivel, PREGUNTAS_EXAMEN)
    import flask
    flask.session['preguntas_actuales'] = preguntas
    flask.session['nivel_actual']       = nivel
    flask.session['modo_examen']        = True
    return render_template('quiz.html', preguntas=preguntas, nivel=nivel, es_examen=True)


# ── Resultado ─────────────────────────────────────────────────────────────────

@app.route('/resultado', methods=['POST'])
@login_required
def resultado():
    import flask
    preguntas  = flask.session.get('preguntas_actuales', [])
    nivel      = flask.session.get('nivel_actual', 'facil')
    es_examen  = flask.session.get('modo_examen', False)

    aciertos = sum(
        1 for i, p in enumerate(preguntas)
        if request.form.get(f'pregunta_{i}') == p['correcta']
    )
    total    = len(preguntas)
    pct      = round((aciertos / total) * 100) if total else 0

    if es_examen:
        aprobado = pct >= 60
    else:
        aprobado = pct >= PCT_APROBAR_NIVEL

    # Actualizar progreso en la BD
    if not es_examen:
        current_user.actualizar_mejor_pct(nivel, pct)
        if aprobado:
            idx = _nivel_idx(nivel)
            if idx + 1 < len(ORDEN_NIVELES):
                siguiente = ORDEN_NIVELES[idx + 1]
                if _nivel_idx(current_user.nivel_desbloqueado) < _nivel_idx(siguiente):
                    current_user.nivel_desbloqueado = siguiente
    else:
        # Los exámenes también guardan el mejor pct (para estadísticas)
        current_user.actualizar_mejor_pct(nivel, pct)

    # Guardar en historial
    reg = Historial(
        user_id  = current_user.id,
        nivel    = ('Examen ' if es_examen else '') + nivel.capitalize(),
        aciertos = aciertos,
        total    = total,
        pct      = pct,
        aprobado = aprobado,
    )
    db.session.add(reg)
    db.session.commit()

    return render_template('resultado.html',
                           aciertos=aciertos, total=total,
                           pct=pct, aprobado=aprobado,
                           nivel=nivel, es_examen=es_examen)


# ── Arranque ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_ENV') == 'development')


# ── PWA ───────────────────────────────────────────────────────────────────────

@app.route('/manifest.json')
def manifest():
    from flask import send_from_directory
    return send_from_directory('static', 'manifest.json',
                               mimetype='application/manifest+json')

@app.route('/sw.js')
def service_worker():
    from flask import send_from_directory, make_response
    resp = make_response(send_from_directory('static', 'sw.js'))
    resp.headers['Content-Type'] = 'application/javascript'
    resp.headers['Service-Worker-Allowed'] = '/'
    return resp

@app.route('/offline')
def offline():
    return render_template('offline.html')
