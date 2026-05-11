# AstroSecurity 🛡️

Plataforma de aprendizaje en ciberseguridad con autenticación real, base de datos en la nube y exámenes completos.

## Características

- ✅ **Cuentas reales** — registro, login y contraseña cifrada con bcrypt
- ✅ **Progreso en la nube** — sincronizado desde cualquier dispositivo
- ✅ **3 Niveles** (Fácil → Intermedio → Avanzado, 10 preguntas c/u)
- ✅ **3 Exámenes** (40 preguntas cada uno, se desbloquean con ≥60% en el nivel)
- ✅ **Historial completo** guardado en PostgreSQL
- ✅ **100% Responsive** — celular, tablet, laptop y desktop
- ✅ **Listo para Render + GitHub**

---

## Despliegue en Render + GitHub

### 1. Sube el proyecto a GitHub

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/astrosecurity.git
git push -u origin main
```

### 2. Crea el Web Service en Render

1. Ve a [render.com](https://render.com) → **New → Web Service**
2. Conecta tu repositorio de GitHub
3. Configura:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`

### 3. Crea la Base de Datos PostgreSQL en Render

1. En Render → **New → PostgreSQL**
2. Asígnale el nombre `astrosecurity-db`
3. Copia el **Internal Database URL**

### 4. Agrega las variables de entorno en el Web Service

En **Environment → Add Environment Variable:**

| Clave          | Valor                                        |
|----------------|----------------------------------------------|
| `DATABASE_URL` | URL interna de tu PostgreSQL (de paso 3)     |
| `SECRET_KEY`   | Una cadena aleatoria larga y segura          |
| `FLASK_ENV`    | `production`                                 |

> 💡 **Tip Render:** También puedes usar el archivo `render.yaml` incluido para configurar todo automáticamente.

### 5. Despliega

Render detectará los cambios automáticamente en cada `git push`.

---

## Desarrollo local

```bash
# 1. Clona e instala
git clone https://github.com/TU_USUARIO/astrosecurity.git
cd astrosecurity
pip install -r requirements.txt

# 2. Configura el .env
cp .env.example .env
# Edita .env con tu SECRET_KEY

# 3. Ejecuta
python app.py
```

La app corre en `http://localhost:5000` usando SQLite local.

---

## Estructura del proyecto

```
astrosecurity/
├── app.py                  # Aplicación principal Flask
├── requirements.txt        # Dependencias Python
├── render.yaml             # Configuración automática Render
├── .env.example            # Variables de entorno de ejemplo
├── .gitignore
├── data/
│   ├── preguntas_facil.py       # 40 preguntas nivel fácil
│   ├── preguntas_intermedio.py  # 40 preguntas nivel intermedio
│   └── preguntas_avanzado.py    # 40 preguntas nivel avanzado
├── static/
│   ├── css/style.css       # Estilos responsive
│   └── img/logo.png
└── templates/
    ├── base.html
    ├── bienvenida.html
    ├── presentacion.html
    ├── registro.html       # ← Nuevo: registro de cuenta real
    ├── login.html          # ← Nuevo: inicio de sesión real
    ├── index.html
    ├── niveles.html        # ← Incluye sección de exámenes
    ├── quiz.html
    ├── resultado.html
    ├── historial.html
    ├── objetivo.html
    └── retroalimentacion.html
```

---

## Lógica de desbloqueo

| Acción                        | Requisito                        |
|-------------------------------|----------------------------------|
| Desbloquear Nivel Intermedio  | ≥80% en Nivel Fácil             |
| Desbloquear Nivel Avanzado    | ≥80% en Nivel Intermedio         |
| Desbloquear Examen Fácil      | ≥60% en Nivel Fácil             |
| Desbloquear Examen Intermedio | ≥60% en Nivel Intermedio         |
| Desbloquear Examen Avanzado   | ≥60% en Nivel Avanzado           |
| Aprobar un Examen             | ≥60% de 40 preguntas             |
