import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.counter = 0

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task.deadline, self.counter, task))
        self.counter += 1

    def get_sorted_tasks(self):
        return [item[3] for item in sorted(self.tasks)]
    
    def clear(self):
        self.tasks = []