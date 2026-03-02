import json
from typing import List
from .models import Task


class TaskStorage:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                return [Task(**item) for item in data]
        except:
            return []

    def save_tasks(self, tasks: List[Task]):
        with open(self.file_path, "w") as f:
            json.dump([task.__dict__ for task in tasks], f)