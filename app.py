import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página
st.set_page_config(page_title="Asistente IA de Entrenamientos", page_icon="🏀", layout="wide")

# 2. Configurar la API de Gemini
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Usamos el modelo optimizado para tareas rápidas
    modelo = genai.GenerativeModel('gemini-1.5-flash') 
except KeyError:
    st.error("Falta configurar la GEMINI_API_KEY en los secretos de Streamlit.")
    st.stop()

def generar_con_gemini(categoria, foco, duracion):
    prompt = f'''
    Actúa como un entrenador experto de básquet formativo (estilo FIBA WABC).
    Diseña una sesión de entrenamiento de {duracion} minutos para la categoría {categoria}.
    El foco principal táctico/técnico de la sesión debe ser: {foco}.
    
    Estructura la respuesta de manera clara utilizando Markdown:
    1. Calentamiento (nombre del drill, duración y descripción breve).
    2. Fase Principal (2 o 3 ejercicios enfocados en el tema principal, con tiempos y explicaciones de la rotación/mecánica).
    3. Vuelta a la calma / Cierre.
    
    No incluyas saludos ni texto innecesario, ve directo al plan de práctica.
    '''
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

# 3. Interfaz de Usuario
st.title("🏀 Generador de Prácticas con Inteligencia Artificial")
st.markdown("Configura los parámetros y la IA armará una rutina a medida.")

with st.sidebar:
    st.header("Configurar Práctica")
    categoria_sel = st.selectbox("Categoría", ["U11", "U13", "U15", "U17"])
    foco_sel = st.selectbox("Foco Principal", [
        "Defensa: Ayudas y Rotaciones", 
        "Ofensiva en Transición (Fast Break)", 
        "Spacing y Movimiento sin balón",
        "Técnica Individual: Finalizaciones"
    ])
    tiempo_sel = st.slider("Duración Total (minutos)", 30, 120, 60, 15)
    
    generar_btn = st.button("Generar con Gemini", type="primary")

if generar_btn:
    with st.spinner(f"Consultando manuales y generando práctica para {categoria_sel}..."):
        try:
            plan_generado = generar_con_gemini(categoria_sel, foco_sel, tiempo_sel)
            st.success("¡Entrenamiento generado con éxito!")
            with st.container(border=True):
                st.markdown(plan_generado)
        except Exception as e:
            st.error(f"Hubo un error al contactar a la IA: {e}")
