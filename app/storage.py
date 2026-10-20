
import json
from pathlib import Path
from typing import Any


def load_tasks(file_path: str = "tasks.json") -> list[dict[str, Any]]:
    """Load tasks from a JSON file."""
    path = Path(file_path)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Format penyimpanan tugas tidak valid.")

    return data


def save_tasks(
    tasks: list[dict[str, Any]],
    file_path: str = "tasks.json",
) -> None:
    """Save tasks to a JSON file."""
    path = Path(file_path)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)
