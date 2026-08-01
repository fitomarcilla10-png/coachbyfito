import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página (Más profesional)
st.set_page_config(page_title="CoachBrain Pro Clone", page_icon="📋", layout="wide", initial_sidebar_state="expanded")

# 2. Configuración de la API
if "GEMINI_API_KEY" not in st.secrets:
    st.error("⚠️ Configura tu GEMINI_API_KEY en Settings > Secrets de Streamlit.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
modelo = genai.GenerativeModel('gemini-3.6-flash') 

# 3. Función de Generación Avanzada (Inyectando la base de datos conceptual)
def generar_sesion_avanzada(categoria, duracion, nivel, foco_principal, foco_secundario):
    prompt = f"""
    Actúa como un Master Coach de básquetbol con acceso absoluto a las metodologías y bases de datos de:
    - Breakthrough Basketball
    - Coaches Clipboard
    - Drills and Plays
    - Online Basketball Drills
    - Hooper University (especialista en acciones 5-out y early offense).
    
    Tu tarea es diseñar un plan de entrenamiento altamente detallado de {duracion} minutos para un equipo categoría {categoria} con un nivel {nivel}.
    
    El FOCO PRINCIPAL de la sesión será: {foco_principal}.
    El FOCO SECUNDARIO será: {foco_secundario}.
    
    ESTRUCTURA OBLIGATORIA DEL PLAN:
    Divide el tiempo total lógicamente. Para cada ejercicio utiliza el siguiente formato exacto:
    
    ### [Nombre del Ejercicio (Inglés/Español)] | ⏱️ [Tiempo en min]
    *   **Fuente/Filosofía Inspirada:** (Ej: Breakthrough Basketball / Hooper University)
    *   **Configuración:** (Cómo se disponen los jugadores en la cancha)
    *   **Ejecución:** (Explicación paso a paso de la rotación o movimiento, incluyendo cómo iniciar un early offense o ejecutar rotaciones defensivas)
    *   **Foco del Entrenador:** (Qué detalles corregir, ej: ángulo de cortina, closeout, etc.)
    
    Distribuye el entrenamiento en:
    1. Activación y Rueda de Pases/Tiro (Early Offense habits).
    2. Construcción del Foco Principal (Drills desglosados).
    3. Situaciones de Juego Real (Ej: 3v3 a 5v5 con condicionantes).
    
    Responde directamente con el plan, sin texto introductorio. Usa negritas y viñetas para facilitar la lectura rápida en cancha.
    """
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

# 4. Interfaz Visual (Estilo Dashboard SaaS)
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: 800; color: #1E3A8A; margin-bottom: 0px;}
    .sub-header {font-size: 1.1rem; color: #6B7280; margin-bottom: 30px;}
    .metric-card {background-color: #F3F4F6; padding: 15px; border-radius: 10px; border-left: 5px solid #1E3A8A;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">📋 Coach Planner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Motor de IA entrenado con Breakthrough Basketball, Coaches Clipboard y Hooper University</p>', unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### ⚙️ Parámetros")
    with st.container(border=True):
        categoria_sel = st.selectbox("Categoría", ["U11", "U13", "U15", "U17", "Primera"])
        nivel_sel = st.select_slider("Nivel Competitivo", options=["Formativo", "Intermedio", "Avanzado"])
        tiempo_sel = st.number_input("Duración (min)", min_value=45, max_value=180, value=90, step=15)
        
    st.markdown("### 🎯 Objetivos")
    with st.container(border=True):
        foco_principal = st.selectbox("Foco Principal", [
            "Ofensiva: Acciones 5-Out y Early Offense",
            "Ofensiva: Transición Rápida (Trenzas y Superioridad)",
            "Defensa: Closeouts y Rotaciones en Ayuda",
            "Defensa: Presión Todo el Campo (Press Break)",
            "Técnica: Finalizaciones con contacto y Tiro"
        ])
        
        foco_secundario = st.selectbox("Foco Secundario", [
            "Toma de decisiones (Read and React)",
            "Balance defensivo",
            "Rebote ofensivo y defensivo",
            "Spacing y cortes al aro (Puerta atrás)"
        ])
        
    st.markdown("<br>", unsafe_allow_html=True)
    generar_btn = st.button("🚀 Generar Plan de Entrenamiento", use_container_width=True, type="primary")

with col2:
    if generar_btn:
        with st.spinner("🧠 Consultando metodologías de Coaches Clipboard y Breakthrough Basketball..."):
            try:
                resultado = generar_sesion_avanzada(categoria_sel, tiempo_sel, nivel_sel, foco_principal, foco_secundario)
                
                # Tarjetas de resumen simulando un dashboard
                st.markdown("### 📊 Resumen de Sesión")
                c1, c2, c3 = st.columns(3)
                c1.markdown(f'<div class="metric-card"><b>Categoría:</b><br>{categoria_sel} ({nivel_sel})</div>', unsafe_allow_html=True)
                c2.markdown(f'<div class="metric-card"><b>Tiempo:</b><br>{tiempo_sel} min</div>', unsafe_allow_html=True)
                c3.markdown(f'<div class="metric-card"><b>Tema:</b><br>{foco_principal.split(":")[0]}</div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Renderizado del plan
                st.markdown("### 📝 Desarrollo de la Práctica")
                with st.container(border=True):
                    st.markdown(resultado)
                    
            except Exception as e:
                st.error(f"Error de generación: {e}")
    else:
        st.info("👈 Configura los parámetros en el panel lateral izquierdo y presiona Generar para armar tu práctica estructurada.")
