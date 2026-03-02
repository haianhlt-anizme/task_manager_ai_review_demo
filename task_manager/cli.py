from .service import TaskService


class CLI:

    def __init__(self, service: TaskService):
        self.service = service

    def run(self):
        while True:
            print("1. Add task")
            print("2. Complete task")
            print("3. Exit")

            choice = input("Choose: ")

            if choice == "1":
                title = input("Title: ")
                self.service.add_task(title)

            elif choice == "2":
                task_id = int(input("Task ID: "))
                self.service.complete_task(task_id)

            elif choice == "3":
                break