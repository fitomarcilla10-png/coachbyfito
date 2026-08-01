import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página
st.set_page_config(page_title="Asistente IA de Entrenamientos", page_icon="🏀", layout="wide")

# 2. Configurar la API de Gemini
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    modelo = genai.GenerativeModel('gemini-1.0-pro')
except KeyError:
    st.error("Falta configurar la GEMINI_API_KEY en los secretos de Streamlit.")
    st.stop()

def generar_sesion_completa(categoria, duracion, foco_fisico, foco_tecnico, foco_tactico):
    prompt = f'''
    Actúa como un entrenador experto de básquet formativo (estilo FIBA WABC).
    Diseña una sesión de entrenamiento COMPLETA de {duracion} minutos para la categoría {categoria}.
    
    La sesión DEBE estar estructurada obligatoriamente en las siguientes 4 fases. Distribuye el tiempo de los {duracion} minutos de forma lógica entre ellas:
    
    1. Calentamiento y Preparación Física (Foco: {foco_fisico})
    2. Desarrollo de Técnica Individual (Foco: {foco_tecnico})
    3. Desarrollo de Táctica de Equipo (Foco: {foco_tactico})
    4. Vuelta a la Calma y Elongación
    
    Para cada ejercicio dentro de las fases, detalla en formato Markdown:
    - **Nombre del ejercicio**
    - **Duración:** (en minutos)
    - **Descripción:** (Mecánica, rotación y correcciones principales)
    
    Ve directo al plan de práctica, estructurado de manera limpia, sin saludos iniciales.
    '''
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

# 3. Interfaz de Usuario
st.title("🏀 Generador de Prácticas Integrales con IA")
st.markdown("Configura los objetivos físicos, técnicos y tácticos para tu sesión.")

with st.sidebar:
    st.header("Configurar Práctica")
    categoria_sel = st.selectbox("Categoría", ["U11", "U13", "U15", "U17"])
    tiempo_sel = st.slider("Duración Total (minutos)", 60, 120, 90, 15)
    
    st.divider()
    st.subheader("Objetivos de la Sesión")
    fisico_sel = st.selectbox("Foco Físico", [
        "Agilidad, Coordinación y Escalera", 
        "Velocidad de Reacción y Sprint", 
        "Fuerza Aplicada (Saltos y Contactos)",
        "Resistencia Intermitente (Cardio específico)"
    ])
    
    tecnico_sel = st.selectbox("Foco Técnico", [
        "Mecánica de Tiro y Finalizaciones", 
        "Dribbling, Cambios de Ritmo y Dirección", 
        "Pases, Recepción y Triple Amenaza",
        "Postura Defensiva y Desplazamientos"
    ])
    
    tactico_sel = st.selectbox("Foco Táctico", [
        "Defensa: Ayudas, Rotaciones y Closeouts", 
        "Ofensiva: Transición y Fast Break (Superioridad)", 
        "Ofensiva: Spacing, Cortes y Puerta Atrás",
        "Defensa: Presión a todo el campo",
        "Ofensiva: Conceptos de Pick and Roll"
    ])
    
    st.divider()
    generar_btn = st.button("Generar Sesión Completa", type="primary")

if generar_btn:
    with st.spinner(f"Diseñando plan integral para {categoria_sel}... esto puede tomar unos segundos."):
        try:
            plan_generado = generar_sesion_completa(
                categoria_sel, tiempo_sel, fisico_sel, tecnico_sel, tactico_sel
            )
            st.success("¡Sesión generada con éxito!")
            with st.container(border=True):
                st.markdown(plan_generado)
        except Exception as e:
            st.error(f"Hubo un error al contactar a la IA: {e}")
