
from app.task_manager import TaskManager


def main() -> None:
    manager = TaskManager()

    while True:
        print("\n=== SECURE TASK MANAGER ===")
        print("1. Tambah tugas")
        print("2. Lihat tugas")
        print("3. Selesaikan tugas")
        print("4. Hapus tugas")
        print("5. Keluar")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            title = input("Judul tugas: ")

            try:
                task = manager.add_task(title)
                print(f"Tugas berhasil ditambahkan dengan ID {task['id']}.")
            except ValueError as error:
                print(f"Input tidak valid: {error}")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("Belum ada tugas.")
            else:
                for task in tasks:
                    status = "Selesai" if task["completed"] else "Belum selesai"
                    print(f"{task['id']}. {task['title']} [{status}]")

        elif choice in ("3", "4"):
            try:
                task_id = int(input("Masukkan ID tugas: "))
            except ValueError:
                print("ID harus berupa angka.")
                continue

            success = (
                manager.complete_task(task_id)
                if choice == "3"
                else manager.delete_task(task_id)
            )

            print(
                "Operasi berhasil."
                if success
                else "Tugas tidak ditemukan."
            )

        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
