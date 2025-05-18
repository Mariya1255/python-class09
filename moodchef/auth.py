# auth.py

import json

DB_FILE = "database.json"

def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def login(username):
    db = load_db()
    if username not in db:
        db[username] = {"mood_history": [], "premium": False}
        save_db(db)
    return db[username]
