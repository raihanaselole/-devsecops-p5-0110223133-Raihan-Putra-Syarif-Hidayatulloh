
from typing import Any

from app.storage import load_tasks, save_tasks
from app.validators import validate_task_title


class TaskManager:
    """Manage tasks and persist changes to JSON storage."""

    def __init__(self, file_path: str = "tasks.json") -> None:
        self.file_path = file_path
        self.tasks: list[dict[str, Any]] = load_tasks(file_path)

    def add_task(self, title: str) -> dict[str, Any]:
        """Add a new task."""
        normalized_title = validate_task_title(title)

        task = {
            "id": max(
                (item.get("id", 0) for item in self.tasks),
                default=0,
            ) + 1,
            "title": normalized_title,
            "completed": False,
        }

        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self) -> list[dict[str, Any]]:
        """Return all tasks."""
        return self.tasks.copy()

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        for task in self.tasks:
            if task.get("id") == task_id:
                task["completed"] = True
                self._save()
                return True

        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        for index, task in enumerate(self.tasks):
            if task.get("id") == task_id:
                del self.tasks[index]
                self._save()
                return True

        return False

    def _save(self) -> None:
        """Persist current tasks."""
        save_tasks(self.tasks, self.file_path)
