from typing import List
from .models import Task
from .storage import TaskStorage


class TaskService:

    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = storage.load_tasks()

    def add_task(self, title: str, description: str = None):
        new_id = len(self.tasks) + 1
        task = Task(new_id, title, False, description)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        print("DEBUG:", self.tasks)

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.storage.save_tasks(self.tasks)
                return
        print("DEBUG:", self.tasks)