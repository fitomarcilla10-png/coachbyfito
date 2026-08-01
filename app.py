import streamlit as st
import google.generativeai as genai
import pandas as pd
from streamlit_drawable_canvas import st_canvas
import datetime

# --- 1. CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="CoachBrain Pro - Sistema Integral", page_icon="🏀", layout="wide")

if "GEMINI_API_KEY" not in st.secrets:
    st.error("⚠️ Configura tu GEMINI_API_KEY en Settings > Secrets.")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- 2. MEMORIA DE LA APP (Session State) ---
if "historial_chat" not in st.session_state:
    st.session_state.historial_chat = []
if "plan_actual" not in st.session_state:
    st.session_state.plan_actual = ""
if "plantel" not in st.session_state:
    st.session_state.plantel = pd.DataFrame({
        "Jugador": ["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"],
        "Asistencia": [False, False, False, False, False],
        "Minutos Jugados": [0, 0, 0, 0, 0]
    })

# --- 3. MOTOR DE GENERACIÓN IA (Con sistema anticaídas) ---
def generar_ciclo_integral(categoria, sesiones, tec_indiv, tec_equipo, tactica):
    prompt = f"""
    Actúa como un Entrenador Jefe experto. Diseña un ciclo de {sesiones} entrenamientos consecutivos para la categoría {categoria}.
    
    Debes integrar estos tres contenidos de forma progresiva a lo largo de las {sesiones} clases:
    1. Contenido Técnico Individual: {tec_indiv}
    2. Contenido Técnico de Equipo: {tec_equipo}
    3. Contenido Táctico Principal: {tactica}
    
    Formato para cada clase (Día 1 al Día {sesiones}):
    ### Clase X
    *   **Técnica Individual (15m):** [Ejercicio y foco]
    *   **Técnica Colectiva (20m):** [Ejercicio y foco]
    *   **Situación Táctica (25m):** [Desarrollo del contenido táctico]
    ---
    """
    
    try:
        # Intento 1: Usar el modelo más rápido y moderno
        modelo = genai.GenerativeModel('gemini-1.5-flash')
        respuesta = modelo.generate_content(prompt)
        return respuesta.text
    except Exception as e:
        try:
            # Intento 2: Si el primero falla, usar el modelo base estable
            modelo_respaldo = genai.GenerativeModel('gemini-1.0-pro')
            respuesta = modelo_respaldo.generate_content(prompt)
            return respuesta.text
        except Exception as e_final:
            return f"❌ Error crítico de API: {e_final}. Por favor, verifica que tu API Key empiece con 'AIza' y haya sido creada en AI Studio."    *   **Técnica Individual (15m):** [Ejercicio y foco]
    *   **Técnica Colectiva (20m):** [Ejercicio y foco]
    *   **Situación Táctica (25m):** [Desarrollo del contenido táctico]
    ---
    '''
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

# --- 5. INTERFAZ GRÁFICA (PESTAÑAS) ---
st.title("🏀 Sistema de Gestión Deportiva Integral")

tab_plan, tab_pizarra, tab_gestion, tab_chat = st.tabs([
    "🗓️ Planificación Metodológica", 
    "🖍️ Pizarra Táctica", 
    "📊 Gestión y Asistencia",
    "💬 Chat IA"
])

# ==========================================
# PESTAÑA 1: PLANIFICACIÓN Y EXPORTACIÓN
# ==========================================
with tab_plan:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### ⚙️ Parámetros del Ciclo")
        with st.container(border=True):
            categoria_sel = st.selectbox("Categoría", ["U11", "U13", "U15", "U17", "Primera"])
            num_sesiones = st.slider("Cantidad de Clases (Ciclo)", 1, 10, 4)
            
            st.markdown("**Contenidos a Desarrollar**")
            tec_indiv = st.text_input("Técnica Individual", placeholder="Ej: Mecánica de tiro")
            tec_equipo = st.text_input("Técnica de Equipo", placeholder="Ej: Pases de contraataque")
            tactica = st.text_input("Contenido Táctico (Eje)", placeholder="Ej: Defensa presionante")
            
            generar_btn = st.button("🚀 Generar Ciclo Integral", type="primary", use_container_width=True)
            
    with col2:
        if generar_btn and tec_indiv and tactica:
            with st.spinner("Procesando ciclo metodológico..."):
                plan = generar_ciclo_integral(categoria_sel, num_sesiones, tec_indiv, tec_equipo, tactica)
                st.session_state.plan_actual = plan
                
        if st.session_state.plan_actual:
            st.markdown("### 📋 Documento de Planificación")
            
            b1, b2 = st.columns(2)
            with b1:
                st.download_button(
                    label="💾 Descargar Planificación (.txt)",
                    data=st.session_state.plan_actual,
                    file_name=f"Planificacion_{categoria_sel}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with b2:
                if st.button("☁️ Guardar en Google Sheets", use_container_width=True):
                    st.info("Próximamente: Conexión con base de datos configurada.")
            
            with st.container(border=True):
                st.markdown(st.session_state.plan_actual)

# ==========================================
# PESTAÑA 2: PIZARRA TÁCTICA INTERACTIVA
# ==========================================
with tab_pizarra:
    st.markdown("### 🖍️ Diseña tus jugadas")
    pizarra_col1, pizarra_col2 = st.columns([3, 1])
    
    with pizarra_col2:
        herramienta = st.radio("Herramienta:", ("Dibujo Libre", "Línea Recta", "Círculo", "Rectángulo"))
        color = st.color_picker("Color del trazo", "#1E3A8A")
        grosor = st.slider("Grosor", 1, 10, 3)
        
        modo_dibujo = "freedraw" if herramienta == "Dibujo Libre" else "line" if herramienta == "Línea Recta" else "circle" if herramienta == "Círculo" else "rect"

    with pizarra_col1:
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  
            stroke_width=grosor,
            stroke_color=color,
            background_color="#f0f0f0",
            update_streamlit=True,
            height=400,
            drawing_mode=modo_dibujo,
            key="pizarra",
        )

# ==========================================
# PESTAÑA 3: GESTIÓN DE PLANTEL
# ==========================================
with tab_gestion:
    st.markdown("### 📊 Control de Asistencia Diario")
    fecha_hoy = datetime.date.today().strftime("%d/%m/%Y")
    st.write(f"**Fecha:** {fecha_hoy}")
    
    df_editado = st.data_editor(
        st.session_state.plantel,
        column_config={
            "Asistencia": st.column_config.CheckboxColumn("¿Asistió hoy?", default=False),
        },
        use_container_width=True,
        num_rows="dynamic"
    )
    
    if st.button("Actualizar Base de Datos"):
        st.session_state.plantel = df_editado
        st.success("¡Datos del plantel actualizados en la memoria!")

# ==========================================
# PESTAÑA 4: CHAT IA
# ==========================================
with tab_chat:
    st.markdown("### 💬 Asistente de Refinamiento")
    for mensaje in st.session_state.historial_chat:
        if mensaje["rol"] == "usuario":
            with st.chat_message("user"):
                st.write(mensaje["contenido"])
        else:
            with st.chat_message("assistant"):
                st.write(mensaje["contenido"])

    if prompt_usuario := st.chat_input("Ej: Ajusta la clase 3 para que sea más intensa..."):
        with st.chat_message("user"):
            st.write(prompt_usuario)
        
        st.session_state.historial_chat.append({"rol": "usuario", "contenido": prompt_usuario})
        
        contexto = f"""
        Plan actual:
        {st.session_state.plan_actual}
        
        El entrenador pide: {prompt_usuario}
        
        Responde ajustando el plan.
        """
        
        with st.spinner("Analizando..."):
            respuesta_chat = modelo.generate_content(contexto)
            with st.chat_message("assistant"):
                st.write(respuesta_chat.text)
            st.session_state.historial_chat.append({"rol": "modelo", "contenido": respuesta_chat.text})
