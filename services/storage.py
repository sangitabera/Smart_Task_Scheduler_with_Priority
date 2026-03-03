import json
import os
from models.task import Task

FILE = "data.json"

def save_tasks(tasks):
    os.makedirs("data", exist_ok=True)
    cleaned_tasks = []
    for task in tasks:
        cleaned_tasks.append(task.to_dict())

    with open(FILE, "w") as f:
        json.dump(cleaned_tasks, f, indent=4)

def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            return [Task.from_dict(item) for item in data]
    except json.JSONDecodeError:
        return []
    