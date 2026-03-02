from task_manager.storage import TaskStorage
from task_manager.service import TaskService
from task_manager.cli import CLI


def main():
    storage = TaskStorage("tasks.json")
    service = TaskService(storage)
    cli = CLI(service)
    cli.run()


if __name__ == "__main__":
    main()