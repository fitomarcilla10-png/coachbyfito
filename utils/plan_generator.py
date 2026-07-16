import random
from typing import List, Dict
from datetime import datetime, timedelta
from dataclasses import dataclass
from exercise_db import ExerciseDatabase, Exercise


@dataclass
class TrainingSession:
    session_number: int
    date: str
    exercises: List[Exercise]
    total_duration: int
    focus_areas: List[str]
    objectives: List[str]


@dataclass
class TrainingPlan:
    category: str
    level: str
    duration_type: str
    total_sessions: int
    sessions: List[TrainingSession]
    start_date: str
    end_date: str


class PlanGenerator:
    def __init__(self, db: ExerciseDatabase = None):
        self.db = db or ExerciseDatabase()
    
    def generate_plan(self, 
                     category: str, 
                     level: str, 
                     duration_type: str,
                     start_date: str = None) -> TrainingPlan:
        duration_info = self.db.get_duration_info(duration_type)
        total_sessions = duration_info['sessions']
        
        if start_date is None:
            start_date = datetime.now().strftime('%Y-%m-%d')
        
        sessions = []
        current_date = datetime.strptime(start_date, '%Y-%m-%d')
        
        for session_num in range(1, total_sessions + 1):
            session = self._generate_session(
                session_num, 
                category, 
                level, 
                current_date
            )
            sessions.append(session)
            
            # Calculate next session date (assuming 3 sessions per week)
            if session_num % 3 == 0:
                current_date += timedelta(days=4)  # Weekend break
            else:
                current_date += timedelta(days=1)
        
        end_date = current_date.strftime('%Y-%m-%d')
        
        return TrainingPlan(
            category=category,
            level=level,
            duration_type=duration_type,
            total_sessions=total_sessions,
            sessions=sessions,
            start_date=start_date,
            end_date=end_date
        )
    
    def _generate_session(self, 
                         session_number: int,
                         category: str, 
                         level: str, 
                         date: datetime) -> TrainingSession:
        # Determine session focus based on session number
        focus_pattern = self._get_focus_pattern(session_number)
        
        exercises = []
        total_duration = 0
        focus_areas = []
        
        for exercise_type, count in focus_pattern.items():
            type_exercises = self.db.filter_exercises(
                category, 
                level, 
                [exercise_type]
            )
            
            if len(type_exercises) > 0:
                selected = random.sample(
                    type_exercises, 
                    min(count, len(type_exercises))
                )
                exercises.extend(selected)
                total_duration += sum(ex.duration for ex in selected)
                
                # Add focus areas from exercises
                for ex in selected:
                    focus_areas.extend(ex.focus)
        
        # Remove duplicates from focus areas
        focus_areas = list(set(focus_areas))
        
        # Generate session objectives
        objectives = self._generate_objectives(session_number, category, level, focus_areas)
        
        return TrainingSession(
            session_number=session_number,
            date=date.strftime('%Y-%m-%d'),
            exercises=exercises,
            total_duration=total_duration,
            focus_areas=focus_areas,
            objectives=objectives
        )
    
    def _get_focus_pattern(self, session_number: int) -> Dict[str, int]:
        # Different patterns for different session types
        patterns = [
            # Session 1: Focus on basics
            {"calentamiento": 2, "tecnica": 3, "fisico": 1, "juego": 1},
            # Session 2: Tactical focus
            {"calentamiento": 2, "tecnica": 2, "tactica": 3, "juego": 1},
            # Session 3: Game focus
            {"calentamiento": 2, "tecnica": 1, "tactica": 2, "juego": 2},
            # Session 4: Physical focus
            {"calentamiento": 2, "tecnica": 2, "fisico": 2, "juego": 1},
            # Session 5: Mixed
            {"calentamiento": 2, "tecnica": 2, "tactica": 2, "fisico": 1, "juego": 1},
            # Session 6: Competition
            {"calentamiento": 2, "tecnica": 1, "tactica": 1, "juego": 3},
        ]
        
        pattern_index = (session_number - 1) % len(patterns)
        return patterns[pattern_index]
    
    def _generate_objectives(self, 
                           session_number: int,
                           category: str,
                           level: str,
                           focus_areas: List[str]) -> List[str]:
        objectives = []
        
        # General objectives based on session number
        if session_number <= 3:
            objectives.append("Consolidar fundamentos técnicos básicos")
        elif session_number <= 6:
            objectives.append("Mejorar comprensión táctica")
        elif session_number <= 9:
            objectives.append("Incrementar intensidad y ritmo")
        else:
            objectives.append("Aplicar conceptos en situaciones de juego")
        
        # Specific objectives based on focus areas
        if "dribbling" in focus_areas:
            objectives.append("Mejorar control de balón en movimiento")
        if "lanzamiento" in focus_areas or "tiro_libre" in focus_areas:
            objectives.append("Incrementar precisión en lanzamientos")
        if "defensa" in focus_areas:
            objectives.append("Mejorar posicionamiento defensivo")
        if "pase" in focus_areas:
            objectives.append("Optimizar precisión y timing en pases")
        if "velocidad" in focus_areas or "agilidad" in focus_areas:
            objectives.append("Desarrollar capacidad física específica")
        if "juego_completo" in focus_areas:
            objectives.append("Aplicar conceptos en situaciones reales de partido")
        
        return objectives
    
    def plan_to_dict(self, plan: TrainingPlan) -> Dict:
        return {
            "category": plan.category,
            "level": plan.level,
            "duration_type": plan.duration_type,
            "total_sessions": plan.total_sessions,
            "start_date": plan.start_date,
            "end_date": plan.end_date,
            "sessions": [
                {
                    "session_number": session.session_number,
                    "date": session.date,
                    "exercises": [
                        {
                            "id": ex.id,
                            "name": ex.name,
                            "description": ex.description,
                            "explanation": ex.explanation,
                            "video": ex.video,
                            "duration": ex.duration,
                            "equipment": ex.equipment,
                            "focus": ex.focus
                        }
                        for ex in session.exercises
                    ],
                    "total_duration": session.total_duration,
                    "focus_areas": session.focus_areas,
                    "objectives": session.objectives
                }
                for session in plan.sessions
            ]
        }
    
    def get_session_summary(self, session: TrainingSession) -> str:
        summary = f"Sesión {session.session_number} - {session.date}\n"
        summary += f"Duración total: {session.total_duration} minutos\n"
        summary += f"Áreas de enfoque: {', '.join(session.focus_areas)}\n"
        summary += f"Objetivos: {', '.join(session.objectives)}\n\n"
        summary += "Ejercicios:\n"
        
        for i, exercise in enumerate(session.exercises, 1):
            summary += f"{i}. {exercise.name} ({exercise.duration} min)\n"
        
        return summary
