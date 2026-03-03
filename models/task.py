from datetime import datetime

class Task:
    def __init__(self, title, description, priority, deadline, created_at=None, status="Pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.created_at = created_at
        self.status = status


    def __lt__(self, other):
        if self.priority == other.priority :
            return self.deadline < other.deadline
        return self.priority < other.priority
    

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "priority": self.priority,
                "deadline": self.deadline.isoformat() if isinstance(self.deadline, datetime) else self.deadline,
                "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
                "status": self.status
                }
    
    @staticmethod
    def from_dict(data):
        from datetime import datetime

        deadline = data["deadline"]
        created_at = data["created_at"]

        if isinstance(deadline, str):
            deadline = datetime.fromisoformat(deadline)

        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)

        return Task(
            data["title"],
            data["description"],
            data["priority"],
            deadline,
            created_at,
            data["status"]
        )
