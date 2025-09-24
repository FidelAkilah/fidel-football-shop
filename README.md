Tugas 2

1. Link PWS : https://fidel-akilah-fidelfootballshop.pbp.cs.ui.ac.id

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




Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab:
Data delivery diperlukan untuk memungkinkan komunikasi antar sistem, integrasi dengan layanan eksternal, dan pertukaran data secara real-time. Komponen seperti frontend, backend, database, dan API third-party perlu bertukar informasi secara efisien. Data delivery juga mendukung pengalaman pengguna yang responsif melalui AJAX requests dan memungkinkan satu backend melayani multiple platforms (web, mobile, desktop) dengan format data yang konsisten.
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab:
JSON lebih baik dan populer karena sintaksnya lebih sederhana, ukuran file lebih kecil, dan memiliki native support di JavaScript. JSON lebih human-readable dan less verbose dibanding XML yang memerlukan opening dan closing tags. Parsing JSON juga lebih cepat dan efisien, tidak memerlukan library tambahan di browser, serta lebih cocok untuk aplikasi web modern yang membutuhkan pertukaran data yang cepat dan ringan.
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab:
Method is_valid() berfungsi untuk memvalidasi data input form sebelum diproses atau disimpan ke database. Method ini melakukan pengecekan terhadap constraint field, tipe data, dan aturan validasi yang didefinisikan dalam form atau model. Kita membutuhkannya untuk keamanan, integritas data (memastikan data sesuai format), dan user experience yang baik (memberikan error message yang jelas jika input tidak valid).
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab:
CSRF token diperlukan untuk melindungi dari serangan Cross-Site Request Forgery, yaitu serangan yang memaksa user melakukan aksi tidak diinginkan di website lain. Tanpa CSRF token, penyerang bisa membuat form malicious di website mereka yang secara otomatis mengirim request ke website target menggunakan session cookies user yang masih aktif. Misalnya, user yang login ke bank bisa dipaksa melakukan transfer uang tanpa sepengetahuannya jika mengunjungi website penyerang yang berisi hidden form dengan action menuju website bank.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Implementasi dimulai dengan membuat model Product yang memiliki field name, price, description, thumbnail, category, stock, dan product_views. Kemudian membuat ProductForm untuk handling input data, diikuti dengan views untuk show_main, create_product, show_xml, show_json, dan detail produk. Setelah itu mengonfigurasi URLs untuk routing dan membuat templates HTML untuk menampilkan data. Terakhir, melakukan migration database dan testing endpoints menggunakan Postman untuk memastikan API XML dan JSON berfungsi dengan baik.
6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada feedback negatif hanya positif. Tutorial yang dibuat oleh asdos sangat komprehensif, terstruktur, dan mudah diikuti.
7. Screenshot xml dan json
https://drive.google.com/drive/folders/1Dz9tsaLHm8KzIh_FLC6Sxsk9oHl6mYJ6?usp=sharing



Tugas 4
1. Apa itu Django AuthenticationForm?
Jawab:
AuthenticationForm adalah form bawaan Django yang khusus digunakan untuk proses login. Form ini memvalidasi apakah username dan password yang dimasukkan pengguna cocok dengan data di database dan apakah akun tersebut aktif. Kelebihannya adalah keamanan dan kemudahan penggunaan karena sudah terintegrasi dengan sistem autentikasi Django. Kekurangannya adalah kurang fleksibel, karena secara default hanya menyediakan kolom username dan password, sehingga memerlukan kustomisasi jika ingin menambahkan fitur seperti "Remember Me".

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikannya?
Jawab:
Autentikasi adalah proses verifikasi identitas (menjawab "Siapa Anda?"), sedangkan otorisasi adalah proses penentuan hak akses setelah identitas terverifikasi (menjawab "Apa yang boleh Anda lakukan?"). Django mengimplementasikan autentikasi melalui django.contrib.auth yang menyediakan model User, form, serta fungsi seperti authenticate() dan login(). Sementara itu, otorisasi diimplementasikan melalui sistem perizinan (permission system) yang mencakup flags (is_staff, is_superuser), grup, dan decorators seperti @login_required.

3. Apa saja kelebihan dan kekurangan session dan cookies?
Jawab:
Cookies menyimpan data di browser klien, sehingga tidak membebani server tetapi tidak aman untuk data sensitif dan memiliki ukuran terbatas. Sebaliknya, session menyimpan data di sisi server dan hanya menempatkan ID unik di cookie klien. Hal ini membuat session jauh lebih aman dan mampu menyimpan data lebih besar, namun kekurangannya adalah membebani sumber daya server dan bisa lebih kompleks untuk dikelola dalam skala besar.

4. Apakah penggunaan cookies aman secara default dan bagaimana Django menanganinya?
Jawab:
Tidak, cookies tidak aman secara default karena rentan terhadap serangan seperti XSS (pencurian data) dan CSRF (pemalsuan permintaan). Django menangani ini dengan berbagai cara: menyediakan proteksi CSRF bawaan ({% csrf_token %}), menggunakan cookie sesi yang ditandatangani secara kriptografis dan berstatus HttpOnly (tidak bisa diakses JavaScript), serta menyediakan pengaturan untuk memberlakukan HTTPS (SESSION_COOKIE_SECURE).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist tugas 4
Jawab:
dengan membuat authentication baru yang berisi views dan URL untuk registrasi, login, dan logout. Untuk registrasi, saya menggunakan UserCreationForm, sedangkan untuk login saya memakai AuthenticationForm yang juga berfungsi untuk mengatur cookie last_login. Selanjutnya, saya menghubungkan model Product ke model User bawaan Django menggunakan ForeignKey. Setelah membuat dummy data untuk dua pengguna, saya memodifikasi template halaman utama untuk menampilkan informasi pengguna ({{ user.username }}) dan cookie last_login secara kondisional menggunakan {% if user.is_authenticated %}. Terakhir, semua perubahan di-commit dan di-push ke GitHub.