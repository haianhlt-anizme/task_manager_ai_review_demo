from task_manager.service import TaskService
from task_manager.storage import TaskStorage


def test_add_task():
    storage = TaskStorage("test.json")
    service = TaskService(storage)
    service.add_task("Test")
    assert len(service.tasks) == 1