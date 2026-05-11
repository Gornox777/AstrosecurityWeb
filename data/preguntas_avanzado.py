preguntas_avanzado = [
    # ── Bloque 1: preguntas anteriores rebalanceadas ──
    {
        "pregunta": "¿Qué garantiza el cifrado de extremo a extremo (E2E) en una comunicación digital?",
        "opciones": ["Que el mensaje llega cifrado solo en el primer y último tramo de la red", "Que únicamente el remitente y el destinatario pueden descifrar el contenido, sin acceso intermedio", "Que los archivos adjuntos se comprimen antes de ser enviados", "Que el servidor de mensajería conserva una copia cifrada para auditorías"],
        "correcta": "Que únicamente el remitente y el destinatario pueden descifrar el contenido, sin acceso intermedio"
    },
    {
        "pregunta": "¿Cómo se define un deepfake en el contexto de la seguridad digital?",
        "opciones": ["Una técnica de cifrado profundo utilizada en comunicaciones gubernamentales", "Contenido audiovisual sintético generado mediante inteligencia artificial para suplantar la identidad de personas reales", "Un tipo de ataque de red que opera en capas profundas del modelo OSI", "Un protocolo de autenticación basado en análisis semántico del lenguaje"],
        "correcta": "Contenido audiovisual sintético generado mediante inteligencia artificial para suplantar la identidad de personas reales"
    },
    {
        "pregunta": "¿Qué ocurre durante un ataque de secuestro de sesión (session hijacking)?",
        "opciones": ["El atacante cierra la sesión del usuario para acceder al panel de administración", "El atacante captura el token de sesión activo y lo reutiliza para acceder a la cuenta sin necesitar la contraseña", "El sistema redirige la sesión activa a un servidor de respaldo controlado por el atacante", "El atacante restablece la contraseña aprovechando el proceso de recuperación de cuenta"],
        "correcta": "El atacante captura el token de sesión activo y lo reutiliza para acceder a la cuenta sin necesitar la contraseña"
    },
    {
        "pregunta": "¿Cuál es la naturaleza de un ataque Man-in-the-Middle (MitM)?",
        "opciones": ["El atacante elimina paquetes de datos entre dos partes para interrumpir la comunicación", "El atacante se interpone de forma encubierta en la comunicación entre dos partes para interceptar o modificar los datos", "El atacante suplanta al servidor DNS para redirigir el tráfico hacia un sitio alternativo", "El atacante inyecta código malicioso en el middleware de la aplicación objetivo"],
        "correcta": "El atacante se interpone de forma encubierta en la comunicación entre dos partes para interceptar o modificar los datos"
    },
    {
        "pregunta": "¿La autenticación biométrica elimina completamente el riesgo de suplantación de identidad?",
        "opciones": ["Sí, ya que los datos biométricos son irrepetibles entre individuos", "No, puede ser vulnerada mediante técnicas avanzadas como el uso de réplicas o datos biométricos robados", "Sí, siempre que se combine con una contraseña alfanumérica de mínimo ocho caracteres", "No, pero únicamente en dispositivos con más de cinco años de antigüedad"],
        "correcta": "No, puede ser vulnerada mediante técnicas avanzadas como el uso de réplicas o datos biométricos robados"
    },
    {
        "pregunta": "¿En qué consiste un ataque de inyección SQL y cuál es su objetivo?",
        "opciones": ["Saturar el servidor de base de datos con peticiones masivas para degradar su rendimiento", "Insertar instrucciones SQL maliciosas en campos de entrada para manipular o extraer datos de la base de datos", "Interceptar las consultas SQL mientras transitan por la red sin cifrar", "Modificar el esquema de la base de datos mediante acceso físico al servidor"],
        "correcta": "Insertar instrucciones SQL maliciosas en campos de entrada para manipular o extraer datos de la base de datos"
    },
    {
        "pregunta": "¿Qué acredita un certificado SSL/TLS en un sitio web?",
        "opciones": ["Que el sitio web ha superado una auditoría de contenidos por parte de una entidad gubernamental", "Que la identidad del servidor ha sido validada por una autoridad certificadora y la comunicación está cifrada", "Que el sitio ha alcanzado un volumen mínimo de tráfico mensual considerado seguro", "Que el desarrollador del sitio ha completado una formación oficial en ciberseguridad"],
        "correcta": "Que la identidad del servidor ha sido validada por una autoridad certificadora y la comunicación está cifrada"
    },
    {
        "pregunta": "¿Cómo se define la superficie de ataque de un sistema informático?",
        "opciones": ["La capacidad máxima de procesamiento disponible antes de que el sistema colapse", "El conjunto total de vectores y puntos vulnerables a través de los cuales un atacante podría intentar comprometer el sistema", "El área geográfica desde la cual se originan la mayoría de los intentos de ataque registrados", "El número de usuarios con acceso administrativo al sistema en un momento dado"],
        "correcta": "El conjunto total de vectores y puntos vulnerables a través de los cuales un atacante podría intentar comprometer el sistema"
    },
    {
        "pregunta": "¿Cuál es el mecanismo de un ataque de denegación de servicio distribuido (DDoS)?",
        "opciones": ["Descifrar las comunicaciones cifradas del servidor objetivo mediante ataques criptográficos coordinados", "Inundar el servidor objetivo con volúmenes masivos de tráfico procedente de múltiples fuentes para dejarlo inoperante", "Infiltrarse en el servidor para eliminar de forma selectiva archivos de configuración críticos", "Engañar al administrador del sistema para que revele las credenciales de acceso al servidor"],
        "correcta": "Inundar el servidor objetivo con volúmenes masivos de tráfico procedente de múltiples fuentes para dejarlo inoperante"
    },
    {
        "pregunta": "¿Qué establece el principio de mínimo privilegio en el diseño de sistemas seguros?",
        "opciones": ["Que los usuarios con mayor antigüedad deben tener acceso irrestricto a todos los recursos del sistema", "Que cada usuario o proceso debe disponer únicamente de los permisos estrictamente necesarios para cumplir su función", "Que los privilegios de acceso deben rotar entre los usuarios de forma periódica y automática", "Que el acceso a sistemas críticos debe estar restringido exclusivamente al equipo de dirección"],
        "correcta": "Que cada usuario o proceso debe disponer únicamente de los permisos estrictamente necesarios para cumplir su función"
    },
    {
        "pregunta": "¿En qué se basa la técnica de esteganografía aplicada a la seguridad digital?",
        "opciones": ["En el cifrado asimétrico de archivos mediante claves de gran longitud para máxima seguridad", "En la ocultación de información dentro de archivos de apariencia inocua, como imágenes, audio o vídeo", "En la fragmentación de datos sensibles distribuidos entre múltiples servidores geográficamente dispersos", "En la generación de firmas digitales para garantizar la autenticidad de documentos electrónicos"],
        "correcta": "En la ocultación de información dentro de archivos de apariencia inocua, como imágenes, audio o vídeo"
    },
    {
        "pregunta": "¿Cuál es la diferencia fundamental entre el cifrado simétrico y el asimétrico?",
        "opciones": ["El cifrado simétrico es exclusivo de redes privadas; el asimétrico aplica solo en redes públicas", "El cifrado simétrico usa la misma clave para cifrar y descifrar; el asimétrico emplea un par de claves pública y privada", "El cifrado simétrico es irompible; el asimétrico admite margen de error en su implementación", "El cifrado simétrico requiere hardware especializado; el asimétrico funciona únicamente por software"],
        "correcta": "El cifrado simétrico usa la misma clave para cifrar y descifrar; el asimétrico emplea un par de claves pública y privada"
    },
    {
        "pregunta": "¿Qué define a una vulnerabilidad de día cero (zero-day)?",
        "opciones": ["Una vulnerabilidad detectada y parcheada en menos de veinticuatro horas tras su descubrimiento", "Una falla de seguridad desconocida para el fabricante que puede ser explotada antes de que exista un parche disponible", "Un fallo crítico introducido intencionalmente en el código fuente por un desarrollador interno", "Una brecha de seguridad presente únicamente en versiones de software con más de cinco años de antigüedad"],
        "correcta": "Una falla de seguridad desconocida para el fabricante que puede ser explotada antes de que exista un parche disponible"
    },
    {
        "pregunta": "¿Cómo opera el envenenamiento de caché DNS (DNS spoofing)?",
        "opciones": ["Sobrecarga los servidores DNS con peticiones masivas hasta provocar su caída", "Introduce registros DNS fraudulentos para redirigir a los usuarios a sitios maliciosos en lugar de los legítimos", "Intercepta las respuestas DNS mientras viajan por la red y las modifica en tránsito", "Registra dominios con nombres similares a los legítimos para confundir a los usuarios"],
        "correcta": "Introduce registros DNS fraudulentos para redirigir a los usuarios a sitios maliciosos en lugar de los legítimos"
    },
    {
        "pregunta": "¿Qué es una botnet y cómo se utiliza en ataques informáticos?",
        "opciones": ["Una infraestructura de servidores seguros utilizada para distribuir actualizaciones de software", "Una red de dispositivos comprometidos controlados de forma remota y coordinada por un atacante para ejecutar ataques a gran escala", "Un conjunto de herramientas de análisis de red usadas por equipos de ciberseguridad defensiva", "Una red privada virtual que enruta el tráfico a través de nodos distribuidos para garantizar el anonimato"],
        "correcta": "Una red de dispositivos comprometidos controlados de forma remota y coordinada por un atacante para ejecutar ataques a gran escala"
    },
    {
        "pregunta": "¿Cuál es el propósito del análisis forense digital tras un incidente de seguridad?",
        "opciones": ["Restaurar inmediatamente los sistemas afectados al estado previo al incidente sin análisis previo", "Recopilar, preservar y analizar evidencia digital para determinar el alcance del incidente e identificar responsabilidades", "Diseñar nuevas políticas de seguridad preventiva para aplicar en el siguiente ejercicio fiscal", "Comunicar el incidente a los medios de forma proactiva para gestionar la reputación de la organización"],
        "correcta": "Recopilar, preservar y analizar evidencia digital para determinar el alcance del incidente e identificar responsabilidades"
    },
    {
        "pregunta": "¿Qué ventaja ofrece el sandboxing en el análisis de software potencialmente malicioso?",
        "opciones": ["Permite ejecutar el software con privilegios elevados para observar todo su comportamiento interno", "Permite ejecutar el software en un entorno aislado para observar su comportamiento sin comprometer el sistema real", "Acelera la detección de amenazas al ejecutar el software en hardware dedicado de alta velocidad", "Facilita la comparación automática del software con bases de datos de firmas de malware conocido"],
        "correcta": "Permite ejecutar el software en un entorno aislado para observar su comportamiento sin comprometer el sistema real"
    },
    {
        "pregunta": "¿Cuál es la función de un token JWT (JSON Web Token) en un sistema de autenticación?",
        "opciones": ["Reemplaza por completo al sistema de contraseñas, eliminando la necesidad de credenciales", "El servidor genera un token firmado criptográficamente que el cliente presenta en cada petición para demostrar su identidad", "Cifra la contraseña del usuario antes de transmitirla al servidor durante el inicio de sesión", "Almacena las preferencias de sesión del usuario de forma persistente en el servidor"],
        "correcta": "El servidor genera un token firmado criptográficamente que el cliente presenta en cada petición para demostrar su identidad"
    },
    {
        "pregunta": "¿Por qué el hashing de contraseñas en bases de datos es una práctica de seguridad esencial?",
        "opciones": ["Permite al administrador del sistema recuperar la contraseña original en caso de que el usuario la olvide", "Almacena una representación irreversible de la contraseña, de modo que una filtración de la base de datos no expone las contraseñas en texto claro", "Reduce el espacio de almacenamiento requerido en la base de datos al comprimir las contraseñas", "Cifra la contraseña de forma reversible para que el servidor pueda verificarla sin almacenarla"],
        "correcta": "Almacena una representación irreversible de la contraseña, de modo que una filtración de la base de datos no expone las contraseñas en texto claro"
    },
    {
        "pregunta": "¿Cuál es el principio central del modelo de seguridad Zero Trust?",
        "opciones": ["No conceder acceso a ningún sistema hasta que el usuario haya completado una formación certificada en ciberseguridad", "No confiar en ninguna entidad por defecto, verificando continuamente la identidad y el contexto de cada acceso, incluso dentro del perímetro de la red interna", "Eliminar por completo el uso de contraseñas en favor de métodos de autenticación exclusivamente biométricos", "Restringir el acceso a sistemas críticos a un número máximo de tres administradores certificados"],
        "correcta": "No confiar en ninguna entidad por defecto, verificando continuamente la identidad y el contexto de cada acceso, incluso dentro del perímetro de la red interna"
    },
    # ── Bloque 2: 20 preguntas nuevas ──
    {
        "pregunta": "¿Qué diferencia al cifrado en reposo del cifrado en tránsito?",
        "opciones": ["El cifrado en reposo aplica solo a archivos temporales; el cifrado en tránsito aplica a archivos permanentes", "El cifrado en reposo protege datos almacenados en discos o bases de datos; el cifrado en tránsito protege datos mientras se transmiten por la red", "El cifrado en reposo usa algoritmos simétricos exclusivamente; el cifrado en tránsito usa solo algoritmos asimétricos", "El cifrado en reposo lo gestiona el usuario final; el cifrado en tránsito lo gestiona el proveedor de internet"],
        "correcta": "El cifrado en reposo protege datos almacenados en discos o bases de datos; el cifrado en tránsito protege datos mientras se transmiten por la red"
    },
    {
        "pregunta": "¿Qué es la ofuscación de código en el contexto del malware?",
        "opciones": ["Una técnica de compresión para reducir el tamaño del archivo ejecutable del malware", "Una técnica para hacer el código difícil de leer o analizar, dificultando su detección por parte de antivirus y analistas", "Un método para cifrar las comunicaciones entre el malware y su servidor de control", "Un procedimiento para eliminar los metadatos del código fuente antes de su distribución"],
        "correcta": "Una técnica para hacer el código difícil de leer o analizar, dificultando su detección por parte de antivirus y analistas"
    },
    {
        "pregunta": "¿Qué papel desempeña la cadena de custodia en un proceso de análisis forense digital?",
        "opciones": ["Establece el orden de prioridad en que los sistemas afectados deben ser restaurados tras el incidente", "Documenta de forma rigurosa el manejo de la evidencia digital para garantizar su integridad y validez legal", "Define los niveles de acceso que los analistas pueden tener sobre los sistemas comprometidos durante la investigación", "Determina el software de análisis forense que debe utilizarse según el tipo de dispositivo afectado"],
        "correcta": "Documenta de forma rigurosa el manejo de la evidencia digital para garantizar su integridad y validez legal"
    },
    {
        "pregunta": "¿Qué caracteriza a un ataque de canal lateral (side-channel attack)?",
        "opciones": ["Explotar vulnerabilidades en protocolos de comunicación de redes inalámbricas de banda lateral", "Obtener información sensible analizando características físicas del sistema, como el consumo eléctrico, el tiempo de respuesta o las emisiones electromagnéticas", "Interceptar las comunicaciones que circulan por canales de red no cifrados ni monitorizados", "Introducir código malicioso a través de librerías de terceros integradas en la aplicación objetivo"],
        "correcta": "Obtener información sensible analizando características físicas del sistema, como el consumo eléctrico, el tiempo de respuesta o las emisiones electromagnéticas"
    },
    {
        "pregunta": "¿En qué consiste la técnica de Pass-the-Hash en ataques a sistemas Windows?",
        "opciones": ["Descifrar el hash de una contraseña mediante ataques de diccionario o fuerza bruta hasta recuperar el texto original", "Utilizar el hash capturado de una contraseña para autenticarse en otros sistemas sin necesidad de conocer la contraseña en texto claro", "Interceptar los hashes de contraseñas mientras se transmiten entre el cliente y el servidor durante el proceso de autenticación", "Generar hashes maliciosos que el sistema de autenticación acepta como válidos por una colisión deliberada"],
        "correcta": "Utilizar el hash capturado de una contraseña para autenticarse en otros sistemas sin necesidad de conocer la contraseña en texto claro"
    },
    {
        "pregunta": "¿Qué es la seguridad por diseño (security by design) en el desarrollo de software?",
        "opciones": ["Aplicar parches de seguridad al software una vez que este ha sido desplegado en producción", "Integrar los principios y controles de seguridad desde las primeras fases del diseño y desarrollo, en lugar de añadirlos como capa posterior", "Diseñar interfaces de usuario que dificulten visualmente la identificación de los controles de seguridad", "Contratar a un equipo externo de seguridad únicamente para la fase de pruebas previas al lanzamiento"],
        "correcta": "Integrar los principios y controles de seguridad desde las primeras fases del diseño y desarrollo, en lugar de añadirlos como capa posterior"
    },
    {
        "pregunta": "¿Qué es una prueba de penetración (pentest) y cuál es su finalidad?",
        "opciones": ["Un análisis automatizado de la configuración de red para detectar puertos abiertos en el perímetro", "Un proceso controlado en el que profesionales autorizados intentan explotar vulnerabilidades de un sistema para identificarlas antes que los atacantes", "Una simulación de ataque DDoS para verificar la capacidad de respuesta de la infraestructura", "Un análisis del código fuente para identificar errores de compilación que puedan afectar al rendimiento"],
        "correcta": "Un proceso controlado en el que profesionales autorizados intentan explotar vulnerabilidades de un sistema para identificarlas antes que los atacantes"
    },
    {
        "pregunta": "¿Cómo protege la función de sal (salt) el almacenamiento de contraseñas hasheadas?",
        "opciones": ["Aumenta la longitud efectiva del hash, haciendo que el almacenamiento en disco sea más eficiente", "Añade un valor aleatorio único a cada contraseña antes de hashearla, evitando que contraseñas iguales produzcan el mismo hash y resistiendo ataques de tablas arcoíris", "Cifra el hash resultante con una clave maestra conocida solo por el administrador del sistema", "Divide el hash en fragmentos que se almacenan en tablas de base de datos separadas para mayor seguridad"],
        "correcta": "Añade un valor aleatorio único a cada contraseña antes de hashearla, evitando que contraseñas iguales produzcan el mismo hash y resistiendo ataques de tablas arcoíris"
    },
    {
        "pregunta": "¿Qué es la escalada de privilegios en el contexto de un ataque informático?",
        "opciones": ["La concesión paulatina de permisos adicionales a un usuario a medida que su antigüedad en la organización aumenta", "La técnica mediante la cual un atacante con acceso limitado consigue obtener permisos de nivel superior, típicamente administrativos", "El proceso de solicitar acceso temporal a recursos restringidos a través del sistema de gestión de identidades", "La configuración automática de permisos elevados para usuarios que superan una evaluación de competencias técnicas"],
        "correcta": "La técnica mediante la cual un atacante con acceso limitado consigue obtener permisos de nivel superior, típicamente administrativos"
    },
    {
        "pregunta": "¿Cuál es el propósito de implementar una política de respuesta ante incidentes (IRP) en una organización?",
        "opciones": ["Establecer las sanciones económicas aplicables a empleados que incumplan las normativas de seguridad interna", "Definir un proceso estructurado para detectar, contener, erradicar y recuperarse de incidentes de seguridad de manera coordinada y eficiente", "Documentar el inventario completo de activos tecnológicos de la organización y su valor económico estimado", "Regular el acceso de proveedores externos a los sistemas internos durante las fases de mantenimiento programado"],
        "correcta": "Definir un proceso estructurado para detectar, contener, erradicar y recuperarse de incidentes de seguridad de manera coordinada y eficiente"
    },
    {
        "pregunta": "¿Qué es la computación cuántica y qué implicaciones tiene para los algoritmos de cifrado actuales?",
        "opciones": ["Es una tecnología que acelera el cifrado simétrico existente sin afectar la seguridad de los algoritmos actuales", "Es un paradigma computacional que, al madurar, podría romper algoritmos asimétricos ampliamente usados como RSA, impulsando el desarrollo de criptografía poscuántica", "Es un método de cifrado basado en principios de mecánica cuántica que ya se usa en redes bancarias de forma generalizada", "Es una forma de hardware especializado que solo incrementa la velocidad de los algoritmos de hashing actuales"],
        "correcta": "Es un paradigma computacional que, al madurar, podría romper algoritmos asimétricos ampliamente usados como RSA, impulsando el desarrollo de criptografía poscuántica"
    },
]
# ── Bloque 3: preguntas adicionales para completar 40 ──
preguntas_avanzado += [
    {
        "pregunta": "¿Qué es un rootkit y por que resulta especialmente peligroso?",
        "opciones": ["Un software que acelera el arranque del sistema operativo", "Un malware que se instala en capas profundas del sistema para ocultar su presencia y la de otros programas maliciosos", "Un tipo de firewall que opera a nivel de kernel para mayor rendimiento", "Un protocolo de actualizacion automatica que opera con privilegios de administrador"],
        "correcta": "Un malware que se instala en capas profundas del sistema para ocultar su presencia y la de otros programas maliciosos"
    },
    {
        "pregunta": "¿Que ventaja ofrece el uso de tokens de acceso de corta duracion frente a tokens de larga duracion?",
        "opciones": ["Reducen la carga de procesamiento en el servidor de autenticacion", "Limitan la ventana de exposicion en caso de que un token sea comprometido", "Permiten que el usuario permanezca conectado sin necesidad de reautenticarse nunca", "Aumentan la velocidad de respuesta de las APIs al eliminar verificaciones adicionales"],
        "correcta": "Limitan la ventana de exposicion en caso de que un token sea comprometido"
    },
    {
        "pregunta": "¿En que consiste un ataque de deserializacion insegura?",
        "opciones": ["Interceptar datos mientras se transmiten entre cliente y servidor antes de que sean serializados", "Explotar el proceso de conversion de datos serializados en objetos para ejecutar codigo arbitrario en el servidor", "Modificar el formato de serializacion de una base de datos para corromper sus registros", "Desencriptar datos cifrados aprovechando vulnerabilidades en el algoritmo de serializacion empleado"],
        "correcta": "Explotar el proceso de conversion de datos serializados en objetos para ejecutar codigo arbitrario en el servidor"
    },
    {
        "pregunta": "¿Que implica la gestion de identidades y accesos (IAM) en una organizacion?",
        "opciones": ["Administrar exclusivamente las contrasenas de los empleados a traves de un portal centralizado", "Definir, controlar y auditar quienes tienen acceso a que recursos, bajo que condiciones y con que nivel de privilegio", "Gestionar la adquisicion e inventario de los dispositivos tecnologicos corporativos", "Supervisar el trafico de red entrante y saliente para detectar anomalias en tiempo real"],
        "correcta": "Definir, controlar y auditar quienes tienen acceso a que recursos, bajo que condiciones y con que nivel de privilegio"
    },
    {
        "pregunta": "¿Que diferencia a un IDS de un IPS en seguridad de redes?",
        "opciones": ["El IDS cifra el trafico analizado; el IPS lo comprime para reducir el ancho de banda consumido", "El IDS detecta y alerta sobre amenazas sin bloquearlas; el IPS detecta y bloquea activamente el trafico malicioso", "El IDS opera en redes inalambricas; el IPS opera exclusivamente en redes cableadas", "El IDS requiere hardware dedicado; el IPS puede ejecutarse como software en cualquier servidor"],
        "correcta": "El IDS detecta y alerta sobre amenazas sin bloquearlas; el IPS detecta y bloquea activamente el trafico malicioso"
    },
    {
        "pregunta": "¿Que es la firma digital y como garantiza la autenticidad de un documento?",
        "opciones": ["Una imagen escaneada de la firma manuscrita del autor adjunta al documento en formato digital", "Un valor criptografico generado con la clave privada del firmante que permite verificar la identidad del autor y la integridad del contenido", "Un sello de tiempo emitido por una autoridad certificadora que indica cuando fue creado el documento", "Un codigo QR incrustado en el documento que redirige a la version original almacenada en el servidor del emisor"],
        "correcta": "Un valor criptografico generado con la clave privada del firmante que permite verificar la identidad del autor y la integridad del contenido"
    },
    {
        "pregunta": "¿Que riesgo representa el uso de librerias de terceros desactualizadas en el desarrollo de software?",
        "opciones": ["Que el software ocupe mas espacio en disco del necesario para su funcionamiento", "Que contengan vulnerabilidades conocidas que los atacantes pueden explotar para comprometer la aplicacion", "Que generen conflictos de licencia que impidan la distribucion comercial del producto final", "Que reduzcan el rendimiento de la aplicacion al no estar optimizadas para versiones recientes del lenguaje"],
        "correcta": "Que contengan vulnerabilidades conocidas que los atacantes pueden explotar para comprometer la aplicacion"
    },
    {
        "pregunta": "¿Como contribuye la segmentacion de red a la contencion de un ataque de ransomware?",
        "opciones": ["Impide que el ransomware cifre archivos al detectar patrones de escritura masiva en el sistema de archivos", "Limita la propagacion lateral del malware al aislar los segmentos afectados del resto de la infraestructura", "Garantiza que los archivos cifrados por el ransomware puedan ser descifrados sin pagar el rescate", "Bloquea automaticamente la comunicacion del ransomware con su servidor de mando y control"],
        "correcta": "Limita la propagacion lateral del malware al aislar los segmentos afectados del resto de la infraestructura"
    },
    {
        "pregunta": "¿Que caracteriza al modelo de responsabilidad compartida en servicios de computacion en la nube?",
        "opciones": ["El proveedor asume plena responsabilidad sobre todos los aspectos de seguridad de los datos del cliente", "La responsabilidad de seguridad se divide entre el proveedor, que protege la infraestructura, y el cliente, que protege sus datos y configuraciones", "El cliente delega toda responsabilidad al proveedor a cambio de una tarifa adicional de seguridad gestionada", "El proveedor y el cliente comparten las mismas credenciales de administracion para facilitar la gestion conjunta"],
        "correcta": "La responsabilidad de seguridad se divide entre el proveedor, que protege la infraestructura, y el cliente, que protege sus datos y configuraciones"
    },
]
