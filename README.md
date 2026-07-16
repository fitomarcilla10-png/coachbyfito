# 🏀 Basketball Training Planner

Una aplicación Streamlit para entrenadores de baloncesto que genera planes de entrenamiento personalizados para diferentes categorías y niveles.

## ✨ Características

- **Generación automática de planes** - Crea planes de entrenamiento desde 1 práctica hasta 1 año completo
- **Múltiples categorías** - Iniciación, Infantil, Cadete, Junior y Sénior
- **Diferentes niveles** - Principiante, Intermedio y Avanzado
- **Base de datos de ejercicios** - Ejercicios con explicaciones detalladas y videos
- **Exportación de planes** - Descarga planes en JSON o formato de texto
- **Interfaz intuitiva** - Diseño fácil de usar para entrenadores

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/basketball-training-app.git
cd basketball-training-app
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 🎯 Uso

1. Ejecuta la aplicación:
```bash
streamlit run app.py
```

2. Abre tu navegador y navega a `http://localhost:8501`

3. **Para generar un plan:**
   - Selecciona la categoría (Iniciación, Infantil, Cadete, Junior, Sénior)
   - Elige el nivel (Principiante, Intermedio, Avanzado)
   - Define la duración (1 Práctica, 1 Semana, 1 Mes, 3 Meses, 1 Año)
   - Selecciona la fecha de inicio
   - Haz clic en "Generar Plan"

4. **Para explorar ejercicios:**
   - Navega a la sección "Explorar Ejercicios"
   - Filtra por categoría, nivel o tipo de ejercicio
   - Visualiza los detalles y videos de cada ejercicio

## 📁 Estructura del Proyecto

```
basketball-training-app/
├── app.py                      # Aplicación principal de Streamlit
├── requirements.txt            # Dependencias de Python
├── README.md                   # Este archivo
├── .gitignore                  # Archivos ignorados por Git
├── data/
│   └── exercises.json         # Base de datos de ejercicios
└── utils/
    ├── exercise_db.py         # Gestión de base de datos de ejercicios
    └── plan_generator.py      # Generador de planes de entrenamiento
```

## 🏀 Categorías Disponibles

- **Iniciación** (6-9 años): Introducción al baloncesto con enfoque en diversión y habilidades básicas
- **Infantil** (10-12 años): Desarrollo de técnica básica y comprensión del juego
- **Cadete** (13-15 años): Perfeccionamiento técnico e introducción a conceptos tácticos
- **Junior** (16-18 años): Desarrollo avanzado de habilidades y preparación para competición
- **Sénior** (18+ años): Nivel competitivo con sistemas complejos y preparación física específica

## 📊 Tipos de Ejercicios

- **Calentamiento**: Ejercicios de preparación física y movilidad
- **Técnica**: Desarrollo de habilidades individuales (dribbling, lanzamiento, pase)
- **Táctica**: Conceptos de equipo y situaciones de juego
- **Físico**: Preparación física específica para baloncesto
- **Juego**: Aplicación práctica en situaciones reales

## 🔧 Personalización

### Agregar nuevos ejercicios

Edita `data/exercises.json` para agregar nuevos ejercicios. Cada ejercicio debe incluir:

- `id`: Identificador único
- `name`: Nombre del ejercicio
- `category`: Lista de categorías aplicables
- `level`: Lista de niveles aplicables
- `description`: Descripción breve
- `explanation`: Explicación detallada
- `video`: URL del video (YouTube u otro)
- `duration`: Duración en minutos
- `equipment`: Lista de material necesario
- `focus`: Lista de áreas de enfoque

### Modificar patrones de entrenamiento

Edita `utils/plan_generator.py` para modificar cómo se generan los planes, especialmente el método `_get_focus_pattern()`.

## 📦 Dependencias

- streamlit==1.35.0 - Framework de la aplicación
- pandas==2.2.2 - Manipulación de datos
- numpy==1.26.4 - Operaciones numéricas
- reportlab==4.2.0 - Generación de PDF
- fpdf==1.7.2 - Generación de documentos
- python-dateutil==2.9.0 - Manejo de fechas

## 🚀 Despliegue

### Streamlit Cloud

1. Sube el código a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. La aplicación se desplegará automáticamente

### Otros servicios

La aplicación puede desplegarse en cualquier servicio que soporte Python, como:
- Heroku
- Railway
- Render
- AWS/GCP/Azure

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 👨‍💻 Autor

Tu Nombre - [tu-email@ejemplo.com]

## 🙏 Agradecimientos

- A la comunidad de baloncesto por inspirar este proyecto
- A Streamlit por proporcionar un framework tan fácil de usar
- A todos los entrenadores que comparten sus conocimientos

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio de GitHub.
