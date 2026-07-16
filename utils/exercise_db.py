import json
import os
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Exercise:
    id: str
    name: str
    category: List[str]
    level: List[str]
    description: str
    explanation: str
    video: str
    duration: int
    equipment: List[str]
    focus: List[str]


class ExerciseDatabase:
    def __init__(self, json_path: str = None):
        if json_path is None:
            json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'exercises.json')
        self.json_path = json_path
        self.exercises = self._load_exercises()
        self.categories = self._load_categories()
        self.levels = self._load_levels()
        self.durations = self._load_durations()
    
    def _load_exercises(self) -> Dict[str, List[Exercise]]:
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        exercises_by_type = {}
        for exercise_type, exercise_list in data['exercises'].items():
            exercises_by_type[exercise_type] = [
                Exercise(**exercise) for exercise in exercise_list
            ]
        
        return exercises_by_type
    
    def _load_categories(self) -> Dict[str, Dict]:
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['categories']
    
    def _load_levels(self) -> Dict[str, Dict]:
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['levels']
    
    def _load_durations(self) -> Dict[str, Dict]:
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['durations']
    
    def get_exercises_by_type(self, exercise_type: str) -> List[Exercise]:
        return self.exercises.get(exercise_type, [])
    
    def filter_exercises(self, 
                        category: str, 
                        level: str, 
                        exercise_types: List[str] = None) -> List[Exercise]:
        if exercise_types is None:
            exercise_types = list(self.exercises.keys())
        
        filtered = []
        for exercise_type in exercise_types:
            for exercise in self.exercises[exercise_type]:
                if category in exercise.category and level in exercise.level:
                    filtered.append(exercise)
        
        return filtered
    
    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        for exercise_type in self.exercises:
            for exercise in self.exercises[exercise_type]:
                if exercise.id == exercise_id:
                    return exercise
        return None
    
    def get_category_names(self) -> List[str]:
        return list(self.categories.keys())
    
    def get_level_names(self) -> List[str]:
        return list(self.levels.keys())
    
    def get_duration_names(self) -> List[str]:
        return list(self.durations.keys())
    
    def get_exercise_types(self) -> List[str]:
        return list(self.exercises.keys())
    
    def get_category_info(self, category: str) -> Dict:
        return self.categories.get(category, {})
    
    def get_level_info(self, level: str) -> Dict:
        return self.levels.get(level, {})
    
    def get_duration_info(self, duration: str) -> Dict:
        return self.durations.get(duration, {})
    
    def get_random_exercises(self, 
                            category: str, 
                            level: str, 
                            count: int = 5,
                            exercise_types: List[str] = None) -> List[Exercise]:
        import random
        
        filtered = self.filter_exercises(category, level, exercise_types)
        if len(filtered) <= count:
            return filtered
        
        return random.sample(filtered, count)
