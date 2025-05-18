# models.py

class User:
    def __init__(self, username, mood=None):
        self.username = username
        self.mood = mood
        self.history = []

    def update_mood(self, mood):
        self.mood = mood
        self.history.append(mood)


class Meal:
    def __init__(self, name, mood_match, ingredients, type_):
        self.name = name
        self.mood_match = mood_match
        self.ingredients = ingredients
        self.type = type_  # veg/non-veg


class RecommendationEngine:
    def __init__(self, meals):
        self.meals = meals

    def recommend(self, mood, diet_type=None):
        results = [m for m in self.meals if m.mood_match == mood]
        if diet_type:
            results = [m for m in results if m.type == diet_type]
        return results
