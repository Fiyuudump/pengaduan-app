### Framework Programming **- Pertemuan 1**

**Fondasi Django & Migrasi ke Class-Based Views (CBV)**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### **1. Tujuan Pembelajaran (Learning Objectives)**

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Memahami dan menjelaskan arsitektur **MVT (Model-View-Template)** dan alur *request-response* pada Django.
* Membuat proyek dan aplikasi Django baru dari awal.
* Mendefinisikan sebuah **Model** sederhana dan melakukan migrasi database.
* Membedakan secara konseptual dan praktis antara **Function-Based Views (FBV)** dan **Class-Based Views (CBV)**.
* Mengimplementasikan *generic* CBV (ListView) untuk menampilkan daftar data sebagai praktik refactoring kode.

#### **2. Studi Kasus Semester: Aplikasi Warga Kelurahan**

Selamat datang di mata kuliah Framework Programming! Sepanjang semester ini, kita akan membangun sebuah proyek nyata secara bertahap: **"Aplikasi Warga Kelurahan"**.

* **Konsep:** Sebuah sistem informasi sederhana untuk mengelola data warga dan pengumuman di lingkungan kelurahan.
* **Tujuan Akhir:** Di akhir semester, aplikasi ini akan memiliki backend API yang solid, yang dapat digunakan oleh berbagai aplikasi klien (seperti aplikasi mobile atau dashboard web modern).
* **Langkah Awal:** Hari ini, kita akan memulai dengan fondasi paling dasar, yaitu membuat sistem untuk menampilkan daftar warga yang terdaftar di kelurahan.

#### **3. Materi Ajar (Teori - sekitar 50 menit)**

**A. Arsitektur Django: The Model-View-Template (MVT) Pattern**

Setiap framework memiliki pola arsitektur, dan Django menggunakan MVT. Anggap saja seperti sebuah restoran yang terorganisir dengan baik:![](data:image/jpeg;base64...)

1. **Model (models.py): Sang Koki & Resep**
   * **Apa itu?** Representasi data Anda dalam bentuk objek Python. Setiap model adalah sebuah tabel di database.
   * **Tugasnya:** Mendefinisikan struktur data (misalnya, seorang warga punya NIK, nama, alamat) dan bagaimana cara berinteraksi dengan database (menyimpan, mengambil, menghapus data). Model adalah satu-satunya sumber kebenaran data Anda.
2. **Template (templates/): Sang Penata Saji (Plating)**
   * **Apa itu?** File HTML dengan sintaks khusus Django.
   * **Tugasnya:** Bertanggung jawab atas presentasi atau tampilan. Ia menerima data dari View dan menampilkannya kepada pengguna dalam format HTML yang menarik. Template tidak boleh berisi logika bisnis yang rumit.
3. **View (views.py): Sang Manajer Restoran**
   * **Apa itu?** Otak dari aplikasi Anda. Berupa fungsi atau *class* Python.
   * **Tugasnya:** Menerima permintaan (request) dari pengguna, berkoordinasi dengan **Model** untuk mengambil data yang diperlukan, lalu memilih **Template** yang tepat untuk menyajikan data tersebut, dan akhirnya mengirimkan hasil jadinya (response) kembali ke pengguna.

Alur Kerja Request-Response:

Pengguna mengetik URL -> urls.py (Resepsionis) mengarahkan ke View (Manajer) -> View meminta data ke Model (Koki) -> Model mengambil data dari Database (Gudang Bahan) -> View memberikan data ke Template (Penata Saji) -> Template menghasilkan HTML -> View mengirim HTML ke Pengguna.

**B. Function-Based Views (FBV): Pendekatan Klasik**

FBV adalah cara paling dasar untuk menulis view di Django. Ini adalah sebuah fungsi Python biasa yang menerima request sebagai argumen dan mengembalikan response.

* **Kelebihan:** Sangat eksplisit dan mudah dipahami untuk logika sederhana. Anda bisa melihat alur kerjanya dari atas ke bawah.
* **Kekurangan:** Cenderung menyebabkan duplikasi kode. Untuk satu set data (misal: Warga), Anda mungkin perlu membuat fungsi terpisah untuk list, detail, create, update, dan delete. Ini tidak efisien dan sulit dikelola pada proyek besar.

**C. Class-Based Views (CBV): Pendekatan Modern & Terstruktur**

CBV adalah pendekatan Object-Oriented Programming (OOP) untuk menulis view. Alih-alih fungsi, kita membuat sebuah *class* yang mewarisi fungsionalitas dari Django.

* **Mengapa CBV?**
  + **Terstruktur:** Logika diorganisir berdasarkan metode HTTP (get, post, dll). Ini sangat penting saat kita beralih ke API.
  + **Dapat Digunakan Kembali (Reusable):** Kita bisa menggunakan *inheritance* untuk memperluas fungsionalitas view tanpa menulis ulang semuanya.
  + **DRY (Don't Repeat Yourself):** Django menyediakan **Generic Class-Based Views**, yaitu sekumpulan *class* siap pakai untuk tugas-tugas umum seperti:
    - ListView: Untuk menampilkan daftar objek.
    - DetailView: Untuk menampilkan satu objek spesifik.
    - CreateView, UpdateView, DeleteView: Untuk menangani form pembuatan, pembaruan, dan penghapusan data.

Hari ini, kita akan fokus pada transisi dari FBV ke ListView untuk merasakan langsung keunggulannya.

#### **4. Sesi Praktikum (Sekitar 70 menit)**

**Tujuan: Membuat Aplikasi Warga & Menampilkan Daftar Warga dengan CBV**

**Langkah 0: Setup Proyek Baru**

1. Buat direktori proyek baru dan aktifkan *virtual environment*.
2. Install Django: pip install django
3. Buat proyek Django: django-admin startproject data\_kelurahan
4. Masuk ke direktori proyek: cd data\_kelurahan
5. Buat aplikasi baru: python manage.py startapp warga
6. Daftarkan aplikasi warga di data\_kelurahan/settings.py pada bagian INSTALLED\_APPS.

Langkah 1: Membuat Model Warga

Buka warga/models.py dan definisikan model untuk data warga.

# warga/models.py
from django.db import models

class Warga(models.Model):
 nik = models.CharField(max\_length=16, unique=True, verbose\_name="Nomor Induk Kependudukan")
 nama\_lengkap = models.CharField(max\_length=100, verbose\_name="Nama Lengkap")
 alamat = models.TextField(verbose\_name="Alamat Tinggal")
 no\_telepon = models.CharField(max\_length=15, blank=True, verbose\_name="Nomor Telepon")
 tanggal\_registrasi = models.DateTimeField(auto\_now\_add=True)

 def \_\_str\_\_(self):
 return self.nama\_lengkap

Langkah 2: Migrasi Database

Di terminal, jalankan perintah berikut untuk membuat tabel Warga di database:

1. python manage.py makemigrations
2. python manage.py migrate

Langkah 3: Mendaftarkan Model ke Admin & Menambah Data Dummy

Agar mudah menambah data, daftarkan model ke situs admin Django.

1. Buka warga/admin.py dan tambahkan:
   # warga/admin.py
   from django.contrib import admin
   from .models import Warga

   admin.site.register(Warga)
2. Buat superuser: python manage.py createsuperuser
3. Jalankan server: python manage.py runserver
4. Buka http://127.0.0.1:8000/admin/, login, dan tambahkan 3-4 data warga sebagai contoh.

Langkah 4: Refactoring dari FBV ke CBV (ListView)

Kita akan langsung membuat versi CBV untuk efisiensi.

1. **Buat Template:**
   * Buat direktori: warga/templates/warga/
   * Buat file warga\_list.html di dalamnya:

<!DOCTYPE html>
<html>
<head>
 <title>Daftar Warga Kelurahan</title>
</head>
<body>
 <h1>Daftar Warga</h1>
 <ul>
 {% for warga in object\_list %}
 <li>{{ warga.nama\_lengkap }} - NIK: {{ warga.nik }}</li>
 {% empty %}
 <li>Belum ada data warga yang terdaftar.</li>
 {% endfor %}
 </ul>
</body>
</html>
*Catatan: Secara default, ListView mengirimkan data ke template dengan nama object\_list.*

1. Buat Class-Based View:
   Buka warga/views.py dan tulis kode berikut:
   # warga/views.py
   from django.views.generic import ListView
   from .models import Warga

   class WargaListView(ListView):
    model = Warga
    # Django secara otomatis akan mencari template di:
    # <nama\_app>/<nama\_model>\_list.html -> warga/warga\_list.html

   *Lihat betapa ringkasnya! ListView sudah menangani logika pengambilan semua data (Warga.objects.all()) dan proses rendering template secara otomatis.*
2. **Konfigurasi URL:**
   * Buat file baru warga/urls.py:

# warga/urls.py
from django.urls import path
from .views import WargaListView

urlpatterns = [
 path('', WargaListView.as\_view(), name='warga-list'),
]

* + Hubungkan URL aplikasi ke URL proyek. Buka data\_kelurahan/urls.py:

# data\_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include # Tambahkan include

urlpatterns = [
 path('admin/', admin.site.urls),
 path('warga/', include('warga.urls')), # Arahkan URL /warga/ ke aplikasi warga
]

**Langkah 5: Verifikasi**

1. Jalankan server: python manage.py runserver
2. Buka browser dan akses http://127.0.0.1:8000/warga/.
3. Anda akan melihat daftar warga yang telah Anda tambahkan melalui halaman admin.

#### **5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)**

**Judul:** Membuat Halaman Detail Warga dengan DetailView

Instruksi:

Sekarang setelah halaman daftar berfungsi, tugas Anda adalah membuat halaman detail untuk menampilkan informasi lengkap satu warga berdasarkan ID-nya, menggunakan generic class-based view DetailView.

**Petunjuk:**

1. **Di views.py:**
   * Impor DetailView dari django.views.generic.
   * Buat class baru WargaDetailView(DetailView) dan atur atribut model = Warga.
2. **Buat Template Baru:**
   * Buat file warga/templates/warga/warga\_detail.html.
   * Di dalam template, Anda bisa mengakses data dengan variabel {{ object }}. Tampilkan semua detail warga (nama, NIK, alamat, dll).
3. **Di urls.py:**
   * Buat path URL baru untuk halaman detail yang menangkap *primary key* (pk): path('<int:pk>/', WargaDetailView.as\_view(), name='warga-detail').
4. **Uji Coba:** Ubah template warga\_list.html agar setiap nama warga menjadi link yang mengarah ke halaman detailnya. Contoh: <a href="{% url 'warga-detail' warga.pk %}">{{ warga.nama\_lengkap }}</a>.

#### **6. Penutup & Preview Pertemuan Berikutnya (5 menit)**

* **Rangkuman:** Hari ini kita telah membangun fondasi proyek "Aplikasi Warga Kelurahan", memahami arsitektur MVT, dan yang terpenting, merasakan efisiensi menggunakan Class-Based Views (ListView) dibandingkan pendekatan tradisional.
* **Preview:** Di pertemuan selanjutnya, kita akan menyelam lebih dalam ke **Django Models**. Kita akan belajar cara membuat relasi data (misalnya, satu warga bisa memiliki beberapa laporan) dan cara mengambil data yang saling terhubung dengan efisien.