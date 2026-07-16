# 🏀 CoachBoard - Baloncesto Assistant

Una herramienta moderna e interactiva en Streamlit diseñada para que entrenadores de baloncesto puedan gestionar estadísticas, planificar jugadas con una pizarra interactiva y registrar el rendimiento de su plantilla.

## 🚀 Características

- **Análisis de Estadísticas**: Gráficos interactivos de barras y métricas rápidas (máximo anotador, mejor reboteador, etc.).
- **Pizarra Táctica**: Simulación de posicionamiento de jugadores en media cancha a través de controles interactivos de coordenadas.
- **Registro de Plantilla**: Formulario dinámico para añadir nuevos jugadores en tiempo real.
- **Diseño Personalizado**: Interfaz oscura deportiva optimizada para Streamlit.

## 🛠️ Instalación y Uso Local

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/TU-USUARIO/mi-entrenador-basket.git
   cd mi-entrenador-basket
   ```

2. **Crear y activar un entorno virtual (Recomendado)**:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

5. Abre tu navegador en la dirección local que te indique la consola (normalmente `http://localhost:8501`).

## 📁 Estructura del Proyecto

```
mi-entrenador-basket/
├── .streamlit/
│   └── config.toml      # Configuración del tema visual (estilo oscuro deportivo)
├── app.py               # Código fuente principal de la aplicación
├── requirements.txt     # Dependencias de Python requeridas
└── README.md            # Documentación del proyecto
```

## 🌐 Despliegue en la Nube (Streamlit Cloud)

Para publicar la aplicación de forma gratuita:
1. Sube este proyecto a tu GitHub.
2. Inicia sesión en [share.streamlit.io](https://share.streamlit.io) usando tu cuenta de GitHub.
3. Haz clic en **Deploy an app**, selecciona tu repositorio y especifica `app.py` como archivo principal.
4. ¡Listo! Tu app estará en línea para cualquier persona.