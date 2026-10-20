# devsecops-p5-0110223133-Raihan-Putra-Syarif-Hidayatulloh
1. Deskripsi

Program ini merupakan aplikasi berbasis Python yang digunakan untuk mengelola daftar tugas. Aplikasi menyediakan fitur menambahkan tugas, menampilkan daftar tugas, mengubah status tugas menjadi selesai, dan menghapus tugas. Data disimpan secara lokal dalam format JSON.

2. Teknologi yang Digunakan
- Bahasa pemrograman: Python 3.12
- Penyimpanan data: JSON
- CI/CD: GitHub Actions
- Static Application Security Testing (SAST): Bandit
- Platform pipeline: Ubuntu Latest

3. Struktur Aplikasi
- app/task_manager.py: logika pengelolaan tugas.
- app/storage.py: penyimpanan dan pembacaan data JSON.
- app/validators.py: validasi judul tugas.
- app/cli.py: antarmuka aplikasi melalui terminal.
- tests/test_task_manager.py: pengujian otomatis fitur aplikasi.
- .github/workflows/devsecops.yml: konfigurasi pipeline DevSecOps.

4. Cara Menjalankan Aplikasi
- Pastikan Python 3.12 atau versi kompatibel sudah terpasang.
- Jalankan aplikasi melalui terminal: python -m app.cli
- Untuk menjalankan unit test: python -m unittest discover -s tests -v

5. Implementasi Pipeline DevSecOps
Pipeline diimplementasikan menggunakan GitHub Actions dan berjalan secara otomatis ketika terjadi push ke branch main atau pull request yang menargetkan branch main.
Pipeline memiliki dua job utama:
- Build and Unit Test: memeriksa sintaks kode Python dan menjalankan pengujian otomatis.
- SAST Scan and Quality Gate: menjalankan Bandit untuk menganalisis potensi kerentanan keamanan pada source code. Quality Gate menggagalkan job jika ditemukan temuan dengan tingkat keparahan medium atau high.

6. Tujuan
Proyek ini bertujuan menerapkan prinsip DevSecOps dengan mengintegrasikan pemeriksaan keamanan otomatis ke dalam pipeline pengembangan perangkat lunak sejak tahap awal.
