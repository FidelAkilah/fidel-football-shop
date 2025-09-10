1. Link PWS : 

2. Bagaimana cara kamu mengimplementasikan checklist?
Jawab: Memulai proyek dan app dengan mengikuti tutorial 0 (membuat repo, direktori lokal, dll), lalu
mendefinisikan model sesuai atribut yang diberikan, lalu migrasi database. Setelah itu menyiapkan
routing dengan membuat urls.py dan memodifikasi file views.py

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:  request --> urls.py --> views.py --> models.py --> HTML --> Response

Request dari client/browser diterima, lalu ke urls.py untuk menentukan url yang cocok. Setelah itu
bersasarkan pola url yang cocok, Django akan memanggil fungsi melalui views.py. Fungsi di views.py
akan berinteraksi dengan database models.py. Setelah logika selesai, views.py akan merender berkas HTML lalu Django mengirim response yang berisi halaman HTML ke browser pengguna

4. Jelaskan peran settings.py dalam proyek Django!
Jawab: 
-Mendefinisikan detail koneksi ke database, 
-mencamtumkan semua aplikasi yang digunakan dalam proyek,
-menentukan konfigurasi URL utama, mengelola kunci rahasia,pengaturan debug dan konfigurasi kemanan
-Mendefiniskan lokasi file statis

5. Bagaimana cara kerja migrasi database di Django?
Jawab: -python manage.py makemigrations memindai file models.py. Django akan membuat file migrasi baru di direktori migrations.
- migrate menjalankan skirp migrasi yang belum diterapkan ke databse.

6. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab: Menurut saya adalah karena Model-View-Template yang dimiliki Django. Pola ini membantu memahami pemisahan tangung jawab dalam aplikasi web

7. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab: Tutorialnya sangat jelas dan terstruktur dengan baik, membuat saya mudah memahami alur kerja Django dari awal hingga akhir. 