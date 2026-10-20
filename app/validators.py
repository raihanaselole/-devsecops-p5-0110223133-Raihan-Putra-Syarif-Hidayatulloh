
def validate_task_title(title: str) -> str:
    """Validate and normalize a task title."""
    if not isinstance(title, str):
        raise ValueError("Judul tugas harus berupa teks.")

    normalized_title = title.strip()

    if not normalized_title:
        raise ValueError("Judul tugas tidak boleh kosong.")

    if len(normalized_title) > 100:
        raise ValueError("Judul tugas maksimal 100 karakter.")

    return normalized_title
