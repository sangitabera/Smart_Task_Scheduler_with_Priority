from datetime import datetime

def calculate_urgency(task):
    time_left = (task.deadline - datetime.now()).total_seconds()
    urgency_score = task.priority

    if time_left < 86400:
        urgency_score -= 1
        return urgency_score