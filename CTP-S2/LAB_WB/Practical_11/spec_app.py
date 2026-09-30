from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    task_id: int
    title: str
    completed: bool = False

class TaskManager:
    """Task Manager application developed via specification-first AI assistance."""
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        new_task = Task(task_id=len(self.tasks) + 1, title=title)
        self.tasks.append(new_task)
        return new_task

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                return True
        return False

if __name__ == "__main__":
    manager = TaskManager()
    t1 = manager.add_task("Complete Lab Workbook")
    manager.complete_task(1)
    print(f"Task ID {t1.task_id}: '{t1.title}' | Completed: {t1.completed}")
