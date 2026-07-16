# Contributing to Basketball Training Planner

¡Gracias por tu interés en contribuir al Basketball Training Planner! Las contribuciones son bienvenidas y apreciadas.

## 🤝 Cómo Contribuir

### Reportar Bugs

Si encuentras un bug, por favor:

1. Verifica si el issue ya existe en el repositorio
2. Si no existe, crea un nuevo issue con:
   - Un título descriptivo
   - Pasos para reproducir el bug
   - Comportamiento esperado vs. comportamiento observado
   - Capturas de pantalla si es aplicable
   - Tu entorno (sistema operativo, versión de Python, etc.)

### Sugerir Nuevas Características

Para sugerir nuevas características:

1. Verifica si la sugerencia ya existe
2. Si no, crea un nuevo issue describiendo:
   - La característica propuesta
   - Por qué sería útil
   - Cómo imaginas que debería funcionar
   - Ejemplos de uso si es posible

### Contribuir Código

#### Configuración del Entorno de Desarrollo

1. Fork el repositorio
2. Clona tu fork:
```bash
git clone https://github.com/tu-usuario/basketball-training-app.git
cd basketball-training-app
```

3. Crea un entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecuta la aplicación:
```bash
streamlit run app.py
```

#### Flujo de Trabajo

1. Crea una rama para tu feature o fix:
```bash
git checkout -b feature/tu-feature-o-fix
```

2. Haz tus cambios siguiendo las guías de estilo
3. Prueba tus cambios exhaustivamente
4. Commit tus cambios con mensajes claros:
```bash
git commit -m "Add: descripción clara de tus cambios"
```

5. Push a tu rama:
```bash
git push origin feature/tu-feature-o-fix
```

6. Crea un Pull Request en GitHub

#### Guías de Estilo

- **Python**: Sigue PEP 8
- **Comentarios**: Usa comentarios claros para código complejo
- **Nombres de variables**: Usa nombres descriptivos en inglés
- **Funciones**: Documenta funciones complejas con docstrings

#### Agregar Nuevos Ejercicios

Para agregar nuevos ejercicios:

1. Edita `data/exercises.json`
2. Agrega el ejercicio siguiendo el formato existente:
```json
{
  "id": "tipo_XXX",
  "name": "Nombre del ejercicio",
  "category": ["categorías aplicables"],
  "level": ["niveles aplicables"],
  "description": "Descripción breve",
  "explanation": "Explicación detallada",
  "video": "URL del video",
  "duration": duración en minutos,
  "equipment": ["material necesario"],
  "focus": ["áreas de enfoque"]
}
```

3. Asegúrate de que el ID sea único
4. Prueba que el ejercicio aparece correctamente en la app

## 📝 Pull Requests

Al crear un Pull Request:

- Usa un título claro y descriptivo
- Describe los cambios que hiciste
- Menciona los issues relacionados (ej: `Fixes #123`)
- Asegúrate de que todos los tests pasen (si hay tests)
- Actualiza la documentación si es necesario

## 🧪 Testing

Si agregas tests:

- Escribe tests para nuevas funcionalidades
- Asegúrate de que los tests existentes pasen
- Usa nombres de tests descriptivos

## 📖 Documentación

Si cambias la funcionalidad:

- Actualiza el README.md si es necesario
- Agrega comentarios en el código si es complejo
- Actualiza los docstrings de las funciones

## 🎯 Áreas de Contribución Sugeridas

- Agregar más ejercicios a la base de datos
- Mejorar la interfaz de usuario
- Agregar nuevas funcionalidades (exportación a PDF, etc.)
- Mejorar la generación de planes
- Agregar tests
- Mejorar la documentación
- Traducir la aplicación a otros idiomas
- Optimizar el rendimiento

## 💬 Comunicación

- Sé respetoso y constructivo en todas las interacciones
- Acepta feedback de manera abierta
- Pregunta si algo no está claro

## 📄 Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la Licencia MIT del proyecto.

## 🙏 Agradecimientos

¡Gracias por contribuir a hacer mejor el Basketball Training Planner!
