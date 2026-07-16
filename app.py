import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="CoachBoard - Baloncesto",
    page_icon="🏀",
    layout="wide"
)

# Inicializar estados de sesión para simular una base de datos temporal
if 'players_db' not in st.session_state:
    st.session_state.players_db = pd.DataFrame([
        {"Jugador": "S. Curry", "Puntos": 28, "Asistencias": 7, "Rebotes": 4, "Posición": "Base"},
        {"Jugador": "L. James", "Puntos": 25, "Asistencias": 8, "Rebotes": 8, "Posición": "Alero"},
        {"Jugador": "N. Jokic", "Puntos": 26, "Asistencias": 9, "Rebotes": 12, "Posición": "Pívot"}
    ])

# Título Principal
st.title("🏀 CoachBoard: Asistente del Entrenador")
st.markdown("Herramienta interactiva para planificar jugadas y analizar estadísticas del equipo.")

# Sidebar - Navegación de la App
st.sidebar.header("Menú del Coach")
menu = st.sidebar.radio(
    "Selecciona una herramienta:",
    ["📊 Análisis de Estadísticas", "📋 Pizarra de Jugadas", "📝 Registro de Jugadores"]
)

# ==========================================
# SECCIÓN 1: ANÁLISIS DE ESTADÍSTICAS
# ==========================================
if menu == "📊 Análisis de Estadísticas":
    st.header("📊 Rendimiento del Equipo")
    
    # KPIs rápidos
    df = st.session_state.players_db
    col1, col2, col3 = st.columns(3)
    col1.metric("Máximo Anotador", f"{df.loc[df['Puntos'].idxmax()]['Jugador']} ({df['Puntos'].max()} pts)")
    col2.metric("Líder Asistencias", f"{df.loc[df['Asistencias'].idxmax()]['Jugador']} ({df['Asistencias'].max()} ast)")
    col3.metric("Líder Rebotes", f"{df.loc[df['Rebotes'].idxmax()]['Jugador']} ({df['Rebotes'].max()} reb)")
    
    st.write("---")
    
    # Gráficos de rendimiento interactivos
    st.subheader("Comparativa de Atributos por Jugador")
    metric_selected = st.selectbox("Selecciona métrica para comparar:", ["Puntos", "Asistencias", "Rebotes"])
    
    fig = px.bar(
        df, 
        x="Jugador", 
        y=metric_selected, 
        color="Posición",
        text_auto=True,
        title=f"Distribución de {metric_selected} en la plantilla",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# SECCIÓN 2: PIZARRA DE JUGADAS
# ==========================================
elif menu == "📋 Pizarra de Jugadas":
    st.header("📋 Pizarra Táctica")
    st.markdown("Configura de manera simulada la posición de tus jugadores en media cancha para explicar una táctica.")

    # Selectores interactivos para posicionar 3 atacantes en la pizarra
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        base_x = st.slider("Base (X)", -10.0, 10.0, 0.0, step=0.5)
        base_y = st.slider("Base (Y)", 0.0, 15.0, 12.0, step=0.5)
    with col_c2:
        alero_x = st.slider("Alero (X)", -10.0, 10.0, -8.0, step=0.5)
        alero_y = st.slider("Alero (Y)", 0.0, 15.0, 8.0, step=0.5)
    with col_c3:
        pivot_x = st.slider("Pívot (X)", -10.0, 10.0, 2.0, step=0.5)
        pivot_y = st.slider("Pívot (Y)", 0.0, 15.0, 3.0, step=0.5)

    # Dibujando la media cancha con Plotly
    fig_court = go.Figure()

    # Añadir línea de fondo y bandas laterales
    fig_court.add_shape(type="rect", x0=-11, y0=0, x1=11, y1=15, line_color="black", fillcolor="rgba(0,0,0,0)")
    # Añadir zona / llave
    fig_court.add_shape(type="rect", x0=-3, y0=0, x1=3, y1=5.8, line_color="black", fillcolor="rgba(240,240,240,0.3)")
    # Añadir el aro (simulado)
    fig_court.add_trace(go.Scatter(x=[0], y=[1.5], mode="markers", marker=dict(size=10, color="orange"), name="Aro"))
    
    # Dibujar la línea de 3 puntos (semi-elipse simplificada)
    theta = np.linspace(0, np.pi, 100)
    three_x = 8.5 * np.cos(theta)
    three_y = 8.5 * np.sin(theta) + 1.5
    fig_court.add_trace(go.Scatter(x=three_x, y=three_y, mode="lines", line=dict(color="gray", dash="dash"), name="Línea de 3"))

    # Graficar Jugadores en base a los sliders de arriba
    fig_court.add_trace(go.Scatter(
        x=[base_x, alero_x, pivot_x],
        y=[base_y, alero_y, pivot_y],
        mode="markers+text",
        text=["Base 1", "Alero 3", "Pívot 5"],
        textposition="top center",
        marker=dict(size=18, color="blue"),
        name="Atacantes"
    ))

    fig_court.update_layout(
        title="Posicionamiento Táctico (Media Cancha)",
        xaxis=dict(range=[-12, 12], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, 16], showgrid=False, zeroline=False),
        width=700,
        height=500,
        showlegend=False
    )

    st.plotly_chart(fig_court, use_container_width=True)
    
    # Notas tácticas
    st.subheader("Instrucciones de la Jugada")
    st.text_area("Escribe aquí las indicaciones para tu equipo:", "Ejemplo: El base inicia penetración buscando pase de escape al alero en la esquina o descarga directa con el pívot rolador.")

# ==========================================
# SECCIÓN 3: REGISTRO DE JUGADORES
# ==========================================
elif menu == "📝 Registro de Jugadores":
    st.header("📝 Gestión de Plantilla")
    st.write("Agrega nuevos jugadores o edita las estadísticas actuales directamente en la tabla.")

    # Formulario para añadir jugador
    with st.form("add_player_form", clear_on_submit=True):
        st.subheader("Añadir Nuevo Jugador")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            new_name = st.text_input("Nombre del Jugador")
            new_pos = st.selectbox("Posición", ["Base", "Escolta", "Alero", "Ala-Pívot", "Pívot"])
        with col_f2:
            new_pts = st.number_input("Puntos Promedio", min_value=0, max_value=100, value=10)
            new_ast = st.number_input("Asistencias Promedio", min_value=0, max_value=50, value=2)
            new_reb = st.number_input("Rebotes Promedio", min_value=0, max_value=50, value=2)
            
        submitted = st.form_submit_value("Guardar Jugador")
        if submitted and new_name:
            # Crear nueva fila y concatenar
            new_row = pd.DataFrame([{"Jugador": new_name, "Puntos": new_pts, "Asistencias": new_ast, "Rebotes": new_reb, "Posición": new_pos}])
            st.session_state.players_db = pd.concat([st.session_state.players_db, new_row], ignore_index=True)
            st.success(f"¡{new_name} agregado con éxito!")
            st.rerun()

    # Mostrar tabla actual
    st.subheader("Plantilla Actual")
    st.dataframe(st.session_state.players_db, use_container_width=True)