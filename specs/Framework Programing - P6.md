### Framework Programming - Pertemuan 6

**Hello, API! Pengenalan Django REST Framework (DRF)**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menginstal dan mengkonfigurasi Django REST Framework (DRF) ke dalam proyek Django yang sudah ada.
* Menjelaskan peran vital **Serializer** sebagai penerjemah data.
* Membuat ModelSerializer sederhana untuk mengubah data dari Model menjadi format JSON.
* Mengimplementasikan *generic view* DRF (ListAPIView) untuk membuat sebuah *endpoint* API yang bersifat *read-only*.
* Mengkonfigurasi URL khusus untuk *endpoint* API.
* Menggunakan dan menjelaskan fitur **Browsable API** yang disediakan oleh DRF untuk pengujian.

#### 2. Studi Kasus Semester: Aplikasi Warga Kelurahan

Pada pertemuan sebelumnya, kita telah memahami *mengapa* API itu penting. Sekarang, saatnya mempraktikkannya. Aplikasi kita akan naik level: selain menyajikan halaman HTML untuk staf kelurahan, kita juga akan membuatnya mampu "berbicara" dalam bahasa JSON.

* **Konsep:** Kita akan mulai membangun lapisan API di atas aplikasi yang sudah ada. Lapisan ini tidak akan menghasilkan HTML, melainkan data mentah yang bisa dikonsumsi oleh aplikasi lain.
* **Tujuan Hari Ini:** Kita akan membuat *endpoint* pertama kita: sebuah URL (misalnya /api/warga/) yang jika diakses, akan menampilkan daftar semua warga dalam format JSON, bukan lagi halaman web.

#### 3. Materi Ajar (Teori - sekitar 50 menit)

**A. Apa itu Django REST Framework (DRF)?**

Django REST Framework (DRF) adalah sebuah *library* atau *toolkit* yang sangat powerful dan fleksibel, yang dirancang khusus untuk membangun Web API di atas framework Django. DRF bukan pengganti Django, melainkan **tambahan** yang menyederhanakan banyak tugas kompleks terkait API, seperti:

* **Serialisasi:** Mengubah tipe data kompleks (seperti Django Model instance) menjadi format JSON, dan sebaliknya.
* **Autentikasi & Otorisasi:** Mengamankan *endpoint* API agar hanya bisa diakses oleh pengguna yang berhak.
* **Dokumentasi Otomatis:** Menyediakan antarmuka yang indah dan interaktif (Browsable API) untuk menguji dan memahami API kita.

Karena kelengkapan fiturnya, DRF telah menjadi standar industri untuk membangun API dengan Django.

**B. Komponen Inti DRF: Serializer**

Jika API adalah pelayan, dan JSON adalah bahasanya, maka **Serializer** adalah penerjemah multibahasa yang sangat cerdas.

* **Tugas Utama:**
  1. **Serialisasi (Python -> JSON):** Menerima data dari Python (misalnya, sebuah QuerySet dari model Warga) dan mengubahnya menjadi format JSON yang bisa dikirim melalui internet.
  2. **Deserialisasi (JSON -> Python):** Menerima data JSON dari klien (misalnya, saat pengguna mengirim form dari aplikasi mobile), memvalidasinya, dan mengubahnya kembali menjadi data Python yang bisa disimpan ke database.
* **ModelSerializer:** Sama seperti ModelForm, DRF menyediakan ModelSerializer yang secara ajaib akan membuat *serializer* dari sebuah Model. Ia akan secara otomatis mendeteksi *field-field* yang ada dan menerapkan aturan validasi dasarnya.

**C. API Views: View Khusus untuk API**

DRF menyediakan serangkaian *Class-Based Views* yang dioptimalkan untuk API. Mereka mirip dengan *generic views* Django, tetapi alih-alih merender HTML, mereka mengembalikan *response* dalam format JSON. Contohnya adalah ListAPIView, yang dirancang khusus untuk menampilkan daftar data (mirip ListView, tapi untuk API).

#### 4. Sesi Praktikum (Sekitar 70 menit)

**Tujuan: Membuat Endpoint API Pertama untuk Daftar Warga**

**Langkah 1: Instalasi dan Konfigurasi DRF**

1. Pastikan *virtual environment* proyek Anda aktif.
2. Install DRF melalui pip:
   pip install djangorestframework
3. Daftarkan DRF ke dalam proyek Anda. Buka data\_kelurahan/settings.py dan tambahkan 'rest\_framework' ke INSTALLED\_APPS.
   # data\_kelurahan/settings.py
   INSTALLED\_APPS = [
    # ...
    'django.contrib.staticfiles',
    'warga', # Aplikasi kita

    # Tambahkan di bawahnya
    'rest\_framework',
   ]

Langkah 2: Membuat File serializers.py

Ini adalah tempat kita akan mendefinisikan semua "penerjemah" data kita.

1. Buat file baru di dalam direktori warga: warga/serializers.py.
2. Isi file tersebut dengan kode berikut:
   # warga/serializers.py
   from rest\_framework import serializers
   from .models import Warga

   class WargaSerializer(serializers.ModelSerializer):
    class Meta:
    model = Warga
    # Tentukan field dari model Warga yang ingin kita ekspos di API
    fields = ['id', 'nik', 'nama\_lengkap', 'alamat', 'no\_telepon']

Langkah 3: Membuat API View

Kita akan membuat view baru yang khusus menangani request ke API.

1. Buka warga/views.py.
2. Impor *library* yang dibutuhkan dari DRF dan *serializer* yang baru kita buat.
3. Tambahkan class view baru di bagian bawah file.
   # warga/views.py
   # ... (impor yang sudah ada) ...

   # Impor baru untuk DRF
   from rest\_framework.generics import ListAPIView
   from .serializers import WargaSerializer

   # ... (class view yang sudah ada untuk HTML) ...

   # --- API VIEWS ---
   class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer\_class = WargaSerializer
   * queryset: Sama seperti di ListView, ini menentukan data apa yang akan ditampilkan.
   * serializer\_class: Memberitahu view untuk menggunakan WargaSerializer sebagai penerjemahnya.

Langkah 4: Konfigurasi URL untuk API

Praktik terbaik adalah memisahkan URL untuk API dari URL untuk web biasa.

1. Buka data\_kelurahan/urls.py dan tambahkan path baru untuk semua URL API kita.
   # data\_kelurahan/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')), # URL untuk web
    path('api/', include('warga.api\_urls')), # URL untuk API
   ]
2. Buat file baru di dalam direktori warga: warga/api\_urls.py.
3. Isi file tersebut dengan URL untuk *endpoint* daftar warga.
   # warga/api\_urls.py
   from django.urls import path
   from .views import WargaListAPIView

   urlpatterns = [
    path('warga/', WargaListAPIView.as\_view(), name='api-warga-list'),
   ]

**Langkah 5: Verifikasi dengan Browsable API**

1. Jalankan server: python manage.py runserver.
2. Buka browser dan akses URL API yang baru: http://127.0.0.1:8000/api/warga/.
3. **Lihat keajaibannya!** Anda tidak akan melihat halaman HTML biasa, melainkan **Browsable API** dari DRF. Ini adalah antarmuka web yang menampilkan data Anda dalam format JSON yang rapi, lengkap dengan header HTTP dan informasi lainnya. Ini adalah alat *debugging* yang sangat kuat.

#### 5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

**Judul:** Membuat Endpoint API Detail Warga

Instruksi:

Anda telah berhasil membuat endpoint untuk menampilkan daftar semua warga. Sekarang, buatlah endpoint baru yang menampilkan detail dari satu warga spesifik berdasarkan ID-nya (misalnya /api/warga/1/).

**Petunjuk:**

1. **View:** Di warga/views.py, impor RetrieveAPIView dari rest\_framework.generics. Buat class view baru (misal: WargaDetailAPIView) yang mewarisi RetrieveAPIView. Atribut queryset dan serializer\_class-nya sama dengan WargaListAPIView.
2. **URL:** Di warga/api\_urls.py, tambahkan path baru yang menangkap *primary key* (<int:pk>) dan arahkan ke view baru Anda.
3. **Uji Coba:** Akses URL seperti http://127.0.0.1:8000/api/warga/1/ (ganti 1 dengan ID warga yang ada di database Anda) dan lihat hasilnya di Browsable API.

#### 6. Penutup & Preview Pertemuan Berikutnya (5 menit)

* **Rangkuman:** Selamat! Hari ini kita telah berhasil membangun *endpoint* API pertama kita. Kita telah belajar cara menginstal DRF, memahami peran krusial **Serializer**, dan melihat betapa mudahnya menyajikan data sebagai JSON menggunakan *generic views* DRF.
* **Preview:** API kita saat ini masih *read-only*. Di pertemuan selanjutnya, kita akan membuatnya menjadi interaktif penuh. Kita akan belajar bagaimana menangani operasi POST (Create), PUT (Update), dan DELETE menggunakan ModelViewSet dan Routers, yang akan menyederhanakan proses pembuatan API CRUD secara dramatis.