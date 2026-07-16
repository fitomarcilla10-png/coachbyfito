import streamlit as st
import json
from datetime import datetime
from utils.exercise_db import ExerciseDatabase
from utils.plan_generator import PlanGenerator


# Page configuration
st.set_page_config(
    page_title="Basketball Training Planner",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .exercise-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f9f9f9;
    }
    .session-header {
        background-color: #1f77b4;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    .objective-item {
        background-color: #e8f4f8;
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #1f77b4;
        border-radius: 4px;
    }
    .focus-tag {
        display: inline-block;
        background-color: #ff6b6b;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        margin: 0.25rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    if 'db' not in st.session_state:
        st.session_state.db = ExerciseDatabase()
    if 'generator' not in st.session_state:
        st.session_state.generator = PlanGenerator(st.session_state.db)
    if 'current_plan' not in st.session_state:
        st.session_state.current_plan = None
    if 'selected_session' not in st.session_state:
        st.session_state.selected_session = None


def render_sidebar():
    st.sidebar.title("⚙️ Configuración")
    
    # Category selection
    categories = st.session_state.db.get_category_names()
    category_display = {cat: st.session_state.db.get_category_info(cat)['name'] 
                       for cat in categories}
    selected_category = st.sidebar.selectbox(
        "Categoría",
        options=list(category_display.keys()),
        format_func=lambda x: category_display[x],
        key="category_select"
    )
    
    # Display category info
    cat_info = st.session_state.db.get_category_info(selected_category)
    st.sidebar.info(f"**Rango de edad:** {cat_info['age_range']}\n\n{cat_info['description']}")
    
    # Level selection
    levels = st.session_state.db.get_level_names()
    level_display = {lvl: st.session_state.db.get_level_info(lvl)['name'] 
                    for lvl in levels}
    selected_level = st.sidebar.selectbox(
        "Nivel",
        options=list(level_display.keys()),
        format_func=lambda x: level_display[x],
        key="level_select"
    )
    
    # Display level info
    lvl_info = st.session_state.db.get_level_info(selected_level)
    st.sidebar.info(lvl_info['description'])
    
    # Duration selection
    durations = st.session_state.db.get_duration_names()
    duration_display = {dur: st.session_state.db.get_duration_info(dur)['name'] 
                       for dur in durations}
    selected_duration = st.sidebar.selectbox(
        "Duración del plan",
        options=list(duration_display.keys()),
        format_func=lambda x: duration_display[x],
        key="duration_select"
    )
    
    # Start date
    start_date = st.sidebar.date_input(
        "Fecha de inicio",
        value=datetime.now(),
        key="start_date"
    )
    
    # Generate button
    if st.sidebar.button("🏀 Generar Plan", use_container_width=True, type="primary"):
        with st.spinner("Generando plan de entrenamiento..."):
            plan = st.session_state.generator.generate_plan(
                selected_category,
                selected_level,
                selected_duration,
                start_date.strftime('%Y-%m-%d')
            )
            st.session_state.current_plan = plan
            st.session_state.selected_session = None
            st.success("¡Plan generado exitosamente!")
    
    return selected_category, selected_level, selected_duration


def render_plan_overview(plan):
    st.markdown('<div class="main-header">📋 Plan de Entrenamiento</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Categoría", st.session_state.db.get_category_info(plan.category)['name'])
    
    with col2:
        st.metric("Nivel", st.session_state.db.get_level_info(plan.level)['name'])
    
    with col3:
        st.metric("Duración", st.session_state.db.get_duration_info(plan.duration_type)['name'])
    
    with col4:
        st.metric("Total Sesiones", plan.total_sessions)
    
    st.markdown(f"**📅 Periodo:** {plan.start_date} a {plan.end_date}")
    
    # Session selector
    st.markdown("---")
    st.markdown("### 📅 Seleccionar Sesión")
    
    session_options = [f"Sesión {s.session_number} - {s.date}" for s in plan.sessions]
    selected_idx = st.selectbox(
        "Elige una sesión para ver detalles:",
        range(len(session_options)),
        format_func=lambda x: session_options[x]
    )
    
    st.session_state.selected_session = plan.sessions[selected_idx]
    
    return plan.sessions[selected_idx]


def render_session_details(session):
    st.markdown(f'<div class="session-header">🏀 Sesión {session.session_number} - {session.date}</div>', 
                unsafe_allow_html=True)
    
    # Session metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Duración Total", f"{session.total_duration} minutos")
    
    with col2:
        st.metric("Ejercicios", len(session.exercises))
    
    # Objectives
    st.markdown("### 🎯 Objetivos de la Sesión")
    for obj in session.objectives:
        st.markdown(f'<div class="objective-item">✓ {obj}</div>', unsafe_allow_html=True)
    
    # Focus areas
    st.markdown("### 🎯 Áreas de Enfoque")
    for focus in session.focus_areas:
        st.markdown(f'<span class="focus-tag">{focus}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Exercises
    st.markdown("### 🏋️ Ejercicios")
    
    for i, exercise in enumerate(session.exercises, 1):
        with st.expander(f"{i}. {exercise.name} ({exercise.duration} min)", expanded=True):
            st.markdown(f"**Descripción:** {exercise.description}")
            st.markdown(f"**Explicación:** {exercise.explanation}")
            
            # Equipment
            if exercise.equipment:
                st.markdown(f"**Material necesario:** {', '.join(exercise.equipment)}")
            
            # Focus areas
            st.markdown(f"**Enfoque:** {', '.join(exercise.focus)}")
            
            # Video
            if exercise.video:
                st.markdown(f"**🎥 Video:** [Ver video]({exercise.video})")
                st.video(exercise.video)
    
    # Download session as JSON
    st.markdown("---")
    session_data = {
        "session_number": session.session_number,
        "date": session.date,
        "objectives": session.objectives,
        "focus_areas": session.focus_areas,
        "exercises": [
            {
                "name": ex.name,
                "description": ex.description,
                "explanation": ex.explanation,
                "video": ex.video,
                "duration": ex.duration,
                "equipment": ex.equipment,
                "focus": ex.focus
            }
            for ex in session.exercises
        ]
    }
    
    st.download_button(
        label="📥 Descargar Sesión (JSON)",
        data=json.dumps(session_data, indent=2, ensure_ascii=False),
        file_name=f"sesion_{session.session_number}_{session.date}.json",
        mime="application/json"
    )


def render_full_plan_export(plan):
    st.markdown("---")
    st.markdown("### 📥 Exportar Plan Completo")
    
    plan_dict = st.session_state.generator.plan_to_dict(plan)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Descargar Plan (JSON)",
            data=json.dumps(plan_dict, indent=2, ensure_ascii=False),
            file_name=f"plan_entrenamiento_{plan.start_date}_{plan.end_date}.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col2:
        # Generate text summary
        summary = f"PLAN DE ENTRENAMIENTO - BALONCESTO\n"
        summary += f"{'='*50}\n\n"
        summary += f"Categoría: {st.session_state.db.get_category_info(plan.category)['name']}\n"
        summary += f"Nivel: {st.session_state.db.get_level_info(plan.level)['name']}\n"
        summary += f"Duración: {st.session_state.db.get_duration_info(plan.duration_type)['name']}\n"
        summary += f"Periodo: {plan.start_date} a {plan.end_date}\n"
        summary += f"Total Sesiones: {plan.total_sessions}\n\n"
        summary += f"{'='*50}\n\n"
        
        for session in plan.sessions:
            summary += st.session_state.generator.get_session_summary(session)
            summary += "\n" + "-"*50 + "\n\n"
        
        st.download_button(
            label="📄 Descargar Resumen (TXT)",
            data=summary,
            file_name=f"resumen_plan_{plan.start_date}_{plan.end_date}.txt",
            mime="text/plain",
            use_container_width=True
        )


def render_exercise_browser():
    st.markdown('<div class="main-header">📚 Explorador de Ejercicios</div>', unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        categories = st.session_state.db.get_category_names()
        category_display = {cat: st.session_state.db.get_category_info(cat)['name'] 
                           for cat in categories}
        selected_category = st.selectbox(
            "Filtrar por categoría",
            options=["Todas"] + list(category_display.keys()),
            format_func=lambda x: category_display.get(x, x)
        )
    
    with col2:
        levels = st.session_state.db.get_level_names()
        level_display = {lvl: st.session_state.db.get_level_info(lvl)['name'] 
                        for lvl in levels}
        selected_level = st.selectbox(
            "Filtrar por nivel",
            options=["Todos"] + list(level_display.keys()),
            format_func=lambda x: level_display.get(x, x)
        )
    
    with col3:
        exercise_types = st.session_state.db.get_exercise_types()
        selected_type = st.selectbox(
            "Filtrar por tipo",
            options=["Todos"] + exercise_types
        )
    
    # Get filtered exercises
    if selected_category == "Todas":
        categories = st.session_state.db.get_category_names()
    else:
        categories = [selected_category]
    
    if selected_level == "Todos":
        levels = st.session_state.db.get_level_names()
    else:
        levels = [selected_level]
    
    if selected_type == "Todos":
        types = st.session_state.db.get_exercise_types()
    else:
        types = [selected_type]
    
    filtered_exercises = []
    for cat in categories:
        for lvl in levels:
            for ex_type in types:
                exercises = st.session_state.db.filter_exercises(cat, lvl, [ex_type])
                filtered_exercises.extend(exercises)
    
    # Remove duplicates
    seen_ids = set()
    unique_exercises = []
    for ex in filtered_exercises:
        if ex.id not in seen_ids:
            seen_ids.add(ex.id)
            unique_exercises.append(ex)
    
    st.markdown(f"**{len(unique_exercises)} ejercicios encontrados**")
    
    # Display exercises
    for exercise in unique_exercises:
        with st.expander(f"🏋️ {exercise.name}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Descripción:** {exercise.description}")
                st.markdown(f"**Explicación:** {exercise.explanation}")
                st.markdown(f"**Duración:** {exercise.duration} minutos")
                st.markdown(f"**Material:** {', '.join(exercise.equipment) if exercise.equipment else 'Ninguno'}")
                st.markdown(f"**Enfoque:** {', '.join(exercise.focus)}")
                st.markdown(f"**Categorías:** {', '.join(exercise.category)}")
                st.markdown(f"**Niveles:** {', '.join(exercise.level)}")
            
            with col2:
                if exercise.video:
                    st.markdown("**🎥 Video:**")
                    st.video(exercise.video)


def main():
    initialize_session_state()
    
    # Page navigation
    page = st.sidebar.radio(
        "Navegación",
        ["🏀 Generar Plan", "📚 Explorar Ejercicios"],
        label_visibility="collapsed"
    )
    
    if page == "🏀 Generar Plan":
        selected_category, selected_level, selected_duration = render_sidebar()
        
        if st.session_state.current_plan:
            plan = st.session_state.current_plan
            session = render_plan_overview(plan)
            render_session_details(session)
            render_full_plan_export(plan)
        else:
            st.markdown("""
            <div style='text-align: center; padding: 2rem;'>
                <h2>🏀 Bienvenido al Generador de Planes de Entrenamiento</h2>
                <p>Selecciona la configuración en el panel lateral y genera tu plan personalizado.</p>
                <p>El sistema creará un plan completo con ejercicios adaptados a tu categoría y nivel.</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif page == "📚 Explorar Ejercicios":
        render_exercise_browser()


if __name__ == "__main__":
    main()
