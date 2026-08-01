# Generador de Prácticas de Básquet Integrales (IA) 🏀

Aplicación web construida con Streamlit y la API de Google Gemini para generar planificaciones de entrenamiento de básquetbol formativo de forma automática y completa (Físico, Técnico y Táctico).

## Archivos incluidos
- `app.py`: El código principal de la aplicación.
- `requirements.txt`: Las dependencias necesarias para que Streamlit funcione.
- `.gitignore`: Archivos que GitHub debe ignorar por seguridad (como tus claves de API).

## Instalación Local
1. Clona o descarga este repositorio.
2. Instala las dependencias en tu terminal: `pip install -r requirements.txt`
3. Crea una carpeta llamada `.streamlit` en la raíz del proyecto.
4. Dentro de esa carpeta, crea un archivo `secrets.toml` con tu nueva clave de API:
   ```toml
   GEMINI_API_KEY = "tu_NUEVA_clave_aqui"
   ```
5. Ejecuta la aplicación: `streamlit run app.py`

## Despliegue en Streamlit Cloud
1. Sube estos archivos a un repositorio en GitHub.
2. Ingresa a Streamlit Community Cloud y crea una nueva app.
3. Ve a `Settings > Secrets` en el panel de control de tu app en Streamlit Cloud.
4. Pega tu clave de API:
   ```toml
   GEMINI_API_KEY = "tu_NUEVA_clave_aqui"
   ```
