
import tempfile
import unittest
from pathlib import Path

from app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = str(Path(self.temp_dir.name) / "tasks.json")
        self.manager = TaskManager(self.file_path)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_add_task(self) -> None:
        task = self.manager.add_task("Belajar DevSecOps")

        self.assertEqual(task["title"], "Belajar DevSecOps")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_reject_empty_title(self) -> None:
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self) -> None:
        task = self.manager.add_task("Membuat pipeline")
        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_delete_task(self) -> None:
        task = self.manager.add_task("Hapus tugas ini")
        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(self.manager.list_tasks(), [])

    def test_tasks_persist_after_reload(self) -> None:
        self.manager.add_task("Tes penyimpanan")
        reloaded_manager = TaskManager(self.file_path)

        self.assertEqual(len(reloaded_manager.list_tasks()), 1)
        self.assertEqual(
            reloaded_manager.list_tasks()[0]["title"],
            "Tes penyimpanan",
        )


if __name__ == "__main__":
    unittest.main()
