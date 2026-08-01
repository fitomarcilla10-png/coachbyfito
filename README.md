# Generador de Prácticas de Básquet (IA) 🏀

Aplicación web construida con Streamlit y la API de Google Gemini para generar planificaciones de entrenamiento de básquetbol formativo de forma automática.

## Archivos incluidos
- `app.py`: El código principal de la aplicación.
- `requirements.txt`: Las dependencias necesarias para que Streamlit funcione.
- `.gitignore`: Archivos que GitHub debe ignorar por seguridad (como tus claves de API).

## Instalación Local

1. Clona o descarga este repositorio.
2. Instala las dependencias en tu terminal: `pip install -r requirements.txt`
3. Crea una carpeta llamada `.streamlit` en la raíz del proyecto.
4. Dentro de esa carpeta, crea un archivo `secrets.toml` con tu clave de API:
   ```toml
   GEMINI_API_KEY = "tu_clave_aqui"
   ```
5. Ejecuta la aplicación: `streamlit run app.py`

## Despliegue en Streamlit Cloud

1. Sube todos estos archivos a un nuevo repositorio en tu cuenta de GitHub.
2. Ingresa a [Streamlit Community Cloud](https://share.streamlit.io/) y crea una nueva app enlazando tu repositorio.
3. Antes de darle a "Deploy", ve a las configuraciones avanzadas o, una vez desplegado, ve a `Settings > Secrets`.
4. Pega tu clave de API exactamente con este formato:
   ```toml
   GEMINI_API_KEY = "tu_clave_aqui"
   ```
5. ¡Listo! Tu app estará funcional y conectada a Gemini.
