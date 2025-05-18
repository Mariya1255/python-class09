from models import Meal

def get_sample_meals():
    return [
        Meal("Chocolate Cake", "Sad", ["chocolate", "sugar", "flour"], "veg"),
        Meal("Spicy Ramen", "angry", ["noodles", "chili", "soy"], "non-veg"),
        Meal("Fruit Smoothie", "happy", ["banana", "milk", "berries"], "veg"),
        Meal("Garlic Soup", "sad", ["garlic", "onion", "broth"], "veg"),
        Meal("Chicken Wrap", "lazy", ["chicken", "tortilla", "veggies"], "non-veg"),
    ]


