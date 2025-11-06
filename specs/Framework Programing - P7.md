### **Modul Pembelajaran - Pertemuan 7**

Mata Kuliah: Framework Programming

Topik: API Interaktif Penuh dengan ViewSet & Routers

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### **1. Tujuan Pembelajaran (Learning Objectives)**

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menjelaskan keuntungan menggunakan ViewSet dibandingkan APIView individual.
* Merefaktor ListAPIView dan RetrieveAPIView yang terpisah menjadi satu ModelViewSet.
* Memahami bagaimana ModelViewSet secara otomatis menyediakan fungsionalitas CRUD penuh.
* Menjelaskan fungsi Router dalam menghasilkan pola URL secara otomatis.
* Mengganti konfigurasi URL manual dengan DefaultRouter dari DRF.
* Menguji semua operasi CRUD (GET, POST, PUT, DELETE) melalui Browsable API.

#### **2. Studi Kasus Semester: Aplikasi Warga Kelurahan**

API kita sudah bisa menyajikan data warga, baik dalam bentuk daftar maupun detail. Namun, API tersebut masih bersifat *read-only* (hanya bisa dibaca). Ini belum cukup untuk aplikasi modern. Klien (seperti aplikasi mobile) harus bisa membuat, mengubah, dan menghapus data melalui API.

* **Konsep:** Daripada membuat *class view* terpisah untuk setiap operasi (Create, Retrieve, Update, Delete), kita akan menggunakan ViewSet untuk menggabungkan semua logika yang terkait dengan satu model ke dalam satu *class* saja. Kemudian, kita akan menggunakan Router untuk secara ajaib membuatkan semua URL yang kita butuhkan.
* **Tujuan Hari Ini:** Mengubah API warga kita dari *read-only* menjadi API dengan fungsionalitas CRUD penuh hanya dengan beberapa baris kode.

#### **3. Materi Ajar (Teori - sekitar 50 menit)**

**A. Efisiensi Kode: Dari APIView ke ViewSet**

Pada pertemuan sebelumnya, kita membuat WargaListAPIView dan WargaDetailAPIView. Jika kita ingin menambahkan fungsionalitas Create, Update, dan Delete, kita harus membuat tiga *class view* lagi. Ini sangat tidak efisien dan membuat kode kita membengkak.

**ViewSet** adalah sebuah abstraksi dari DRF yang memungkinkan kita menggabungkan logika untuk beberapa *view* yang saling terkait (seperti semua operasi untuk model Warga) ke dalam **satu class tunggal**.

* **ModelViewSet:** Ini adalah ViewSet paling *powerful* yang disediakan DRF. Ia mewarisi fungsionalitas dari *generic views* dan secara otomatis menyediakan implementasi lengkap untuk semua aksi CRUD standar:
  + .list() (GET untuk daftar)
  + .retrieve() (GET untuk detail)
  + .create() (POST untuk membuat)
  + .update() (PUT untuk memperbarui)
  + .partial\_update() (PATCH untuk memperbarui sebagian)
  + .destroy() (DELETE untuk menghapus)

Hanya dengan mendefinisikan queryset dan serializer\_class, ModelViewSet akan menangani semua logika di belakang layar.

**B. URL Otomatis: Keajaiban Router**

Setelah menggabungkan logika ke dalam ViewSet, bagaimana kita membuat URL untuk setiap aksi? Membuatnya satu per satu di urls.py akan mengalahkan tujuan efisiensi kita.

**Router** adalah komponen DRF yang secara otomatis menghasilkan konfigurasi URL untuk sebuah ViewSet.

* **Cara Kerja:** Anda cukup "mendaftarkan" ViewSet Anda ke sebuah Router. Router kemudian akan memeriksa semua aksi yang tersedia di ViewSet tersebut dan membuat pola URL yang sesuai dengan konvensi RESTful.
* **DefaultRouter:** Ini adalah Router yang paling umum digunakan. Selain menghasilkan URL untuk ViewSet, ia juga secara otomatis membuat halaman *root* API (misalnya di /api/) yang menampilkan daftar semua *endpoint* yang terdaftar. Ini sangat membantu dalam navigasi dan eksplorasi API.

Contoh URL yang akan dibuat oleh Router untuk ViewSet Warga:

* /api/warga/ -> GET (list), POST (create)
* /api/warga/{pk}/ -> GET (retrieve), PUT (update), PATCH (partial update), DELETE (destroy)

#### **4. Sesi Praktikum (Sekitar 70 menit)**

**Tujuan: Mengubah API Warga Menjadi API CRUD Penuh**

**Langkah 1: Merefaktor views.py untuk Menggunakan ModelViewSet**

1. Buka warga/views.py.
2. Impor viewsets dari rest\_framework.
3. Hapus atau komentari *class* WargaListAPIView dan WargaDetailAPIView yang lama.
4. Ganti dengan satu ViewSet yang ringkas ini:
   # warga/views.py
   # ... (impor Django & form yang sudah ada) ...

   # Impor baru untuk DRF
   from rest\_framework import viewsets # Impor viewsets
   from .serializers import WargaSerializer
   from .models import Warga

   # ... (class view untuk HTML) ...

   # --- API VIEWS ---
   class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Warga.objects.all().order\_by('-tanggal\_registrasi')
    serializer\_class = WargaSerializer

   *Hanya itu! Class tunggal ini sekarang menangani semua logika CRUD untuk model Warga.*

**Langkah 2: Merefaktor api\_urls.py untuk Menggunakan Router**

1. Buka warga/api\_urls.py.
2. Hapus semua kode yang ada dan ganti dengan kode berikut:
   # warga/api\_urls.py
   from django.urls import path, include
   from rest\_framework.routers import DefaultRouter
   from .views import WargaViewSet

   # Buat sebuah router dan daftarkan ViewSet kita
   router = DefaultRouter()
   router.register(r'warga', WargaViewSet, basename='warga')

   # URL API sekarang ditentukan secara otomatis oleh router.
   urlpatterns = [
    path('', include(router.urls)),
   ]
   * router.register(r'warga', ...): Mendaftarkan WargaViewSet ke router dengan prefix URL warga.

**Langkah 3: Verifikasi dan Uji Coba CRUD**

1. Jalankan server dan buka browser.
2. Akses halaman *root* API: http://127.0.0.1:8000/api/. Anda akan melihat link ke *endpoint* warga yang dibuat oleh DefaultRouter.
3. Klik link tersebut atau akses langsung http://127.0.0.1:8000/api/warga/.
   * **Perhatikan:** Halaman Browsable API sekarang memiliki formulir HTML di bagian bawah untuk **membuat (POST)** warga baru.
4. **Uji CREATE:** Isi formulir dan klik "POST". Anda akan melihat data baru ditambahkan ke daftar.
5. Akses halaman detail salah satu warga, misal http://127.0.0.1:8000/api/warga/1/.
   * **Perhatikan:** Halaman ini sekarang memiliki tombol **DELETE** dan formulir yang terisi penuh untuk operasi **UPDATE (PUT)**.
6. **Uji UPDATE:** Ubah salah satu data di formulir dan klik "PUT". Verifikasi bahwa data telah berubah.
7. **Uji DELETE:** Klik tombol "DELETE" dan konfirmasikan. Verifikasi bahwa data tersebut telah hilang dari daftar.

#### **5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)**

**Judul:** Membuat API CRUD Penuh untuk Pengaduan

Instruksi:

Terapkan pola ViewSet dan Router yang baru saja Anda pelajari untuk membuat API CRUD penuh untuk model Pengaduan.

**Petunjuk:**

1. **Serializer:** Buat PengaduanSerializer di warga/serializers.py untuk model Pengaduan.
2. **ViewSet:** Buat PengaduanViewSet di warga/views.py yang menggunakan ModelViewSet.
3. **Router:** Di warga/api\_urls.py, daftarkan PengaduanViewSet ke *router* yang sama yang sudah ada. Contoh: router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan').
4. **Uji Coba:** Buka /api/pengaduan/ dan lakukan semua operasi CRUD (Create, Read, Update, Delete) untuk data pengaduan melalui Browsable API.

#### **6. Penutup & Preview Pertemuan Berikutnya (5 menit)**

* **Rangkuman:** Hari ini kita telah melakukan refactoring besar yang membuat kode API kita jauh lebih bersih, ringkas, dan profesional. Dengan ModelViewSet dan Router, kita bisa membuat *endpoint* CRUD penuh dalam hitungan menit. Ini adalah cara standar dan paling efisien dalam membangun API dengan DRF.
* **Preview Pertemuan 8 (UTS):** Pertemuan selanjutnya adalah **Ujian Tengah Semester**. Materi akan mencakup semua yang telah kita pelajari dari pertemuan 1 hingga 7, mulai dari konsep Django Lanjutan (CBV, Forms), konsep fundamental API (REST, JSON), hingga dasar-dasar DRF (Serializer, APIView, ViewSet, Router).
* **Preview Pasca-UTS:** Setelah UTS, kita akan memasuki topik yang sangat krusial: **Keamanan API**. Bagaimana cara memastikan hanya pengguna yang terautentikasi yang bisa membuat pengaduan? Dan bagaimana memastikan seorang warga hanya bisa mengedit pengaduannya sendiri? Kita akan membahas **Authentication & Permissions**.