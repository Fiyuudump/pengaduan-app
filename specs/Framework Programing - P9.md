# Framework Programming - P9 Specification

## Topic: Mengamankan API dengan Autentikasi & Permissions

### Overview
Mata Kuliah: Framework Programming  
Topik: Mengamankan API dengan Autentikasi & Permissions  
Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:
- Membedakan konsep **Autentikasi (Authentication)** dan **Otorisasi (Authorization/Permissions)**
- Menjelaskan cara kerja **Token Authentication** sebagai metode standar untuk mengamankan API
- Mengimplementasikan endpoint untuk mendapatkan auth token di DRF
- Menggunakan auth token di API Client (Postman) untuk mengakses endpoint yang terproteksi
- Menerapkan berbagai permission classes bawaan DRF, seperti IsAuthenticated dan IsAuthenticatedOrReadOnly, baik secara global maupun per-view

### Studi Kasus
API kita sudah memiliki fungsionalitas CRUD penuh. Namun, saat ini ada celah keamanan yang sangat besar: **siapa pun di internet bisa mengakses, menambah, mengubah, dan bahkan menghapus data warga dan pengaduan!** Ini tentu tidak bisa diterima di aplikasi nyata.

Kita perlu membangun "gerbang keamanan" untuk API kita. Gerbang ini akan memiliki dua lapis pemeriksaan: pertama, ia akan menanyakan "Siapa Anda?" (Autentikasi), dan kedua, setelah tahu siapa Anda, ia akan memeriksa "Apa yang boleh Anda lakukan?" (Otorisasi/Permissions).

---

## Section 4: Sesi Praktikum (Sekitar 70 menit)

**Tujuan: Mengimplementasikan Token Authentication pada API Kelurahan**

### Langkah 1: Mengaktifkan Aplikasi Token

1. Buka `data_kelurahan/settings.py`
2. Tambahkan `rest_framework.authtoken` ke `INSTALLED_APPS`:
```python
# data_kelurahan/settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',  # Tambahkan ini
]
```
3. Jalankan migrasi untuk membuat tabel yang akan menyimpan token:
```bash
python manage.py migrate
```

### Langkah 2: Membuat Endpoint untuk Mendapatkan Token

1. Buka `data_kelurahan/urls.py` (file URL proyek utama)
2. Impor `obtain_auth_token` dari DRF dan tambahkan path URL baru:
```python
# data_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Impor ini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
    path('api/', include('warga.api_urls')),
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),  # Tambahkan ini
]
```

### Langkah 3: Menetapkan Kebijakan Keamanan Global

Mari kita buat API kita aman secara default.

1. Buka `data_kelurahan/settings.py`
2. Tambahkan konfigurasi `REST_FRAMEWORK` di bagian bawah file:
```python
# data_kelurahan/settings.py
# ... (di bagian paling bawah file) ...
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

*Ini berarti, secara default, semua endpoint API kita sekarang memerlukan token yang valid.*

### Langkah 4: Pengujian di Postman

#### 1. Coba Akses Tanpa Token (Harus Gagal)
- Jalankan server
- Di Postman, buat request GET ke `http://127.0.0.1:8000/api/warga/`
- Klik "Send". Anda akan menerima respons **Status: 401 Unauthorized** dengan pesan "Authentication credentials were not provided." Ini bagus! Keamanan kita berfungsi.

#### 2. Minta Token
- Buat superuser jika Anda belum punya:
```bash
python manage.py createsuperuser
```
- Di Postman, buat request POST ke `http://127.0.0.1:8000/api/auth/token/`
- Pindah ke tab "Body", pilih "raw" dan "JSON"
- Masukkan username dan password Anda:
```json
{"username": "namaadmin", "password": "passwordadmin"}
```
- Klik "Send". Anda akan menerima respons 200 OK dengan token Anda. **Copy token tersebut!**

#### 3. Akses dengan Token (Harus Berhasil)
- Kembali ke request GET untuk `/api/warga/`
- Pindah ke tab "Authorization"
- Pilih "Type": "Auth Token"
- Paste token Anda ke dalam field "Token"
- Klik "Send". Sekarang Anda akan mendapatkan respons 200 OK dengan daftar warga.

### Langkah 5: Melonggarkan Izin untuk View Tertentu

Bagaimana jika kita ingin publik bisa melihat daftar warga, tapi hanya staf yang bisa mengubahnya? Kita bisa menimpa pengaturan global.

1. Buka `warga/views.py`
2. Impor `IsAuthenticatedOrReadOnly` dan tambahkan sebagai `permission_classes` di `WargaViewSet`:
```python
# warga/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # Impor ini
from .serializers import WargaSerializer
from .models import Warga

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Timpa izin default

# ... (PengaduanViewSet masih menggunakan izin default IsAuthenticated) ...
```

3. **Verifikasi Ulang:** Di Postman, coba lagi akses GET `/api/warga/` **tanpa** token. Sekarang seharusnya berhasil. Tapi jika Anda mencoba POST ke URL yang sama tanpa token, itu akan gagal.

---

## Section 5: Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

### Judul: Menerapkan Kebijakan Izin yang Berbeda

Saat ini, `PengaduanViewSet` masih menggunakan izin global (`IsAuthenticated`), yang berarti hanya staf yang bisa melihat atau mengubah data pengaduan. Ini sudah cukup baik.

#### Tugas Anda adalah:

1. **Buat Pengguna Non-Staff**
   - Buat satu pengguna baru melalui halaman admin Django
   - **Jangan** centang status "staff"
   - Simpan pengguna tersebut

2. **Dapatkan Token untuk Pengguna Non-Staff**
   - Gunakan Postman untuk mendapatkan token untuk pengguna non-staf tersebut
   - POST ke `/api/auth/token/` dengan kredensial pengguna non-staff
   - Simpan token yang diterima

3. **Test Akses dengan Token Non-Staff**
   - Coba gunakan token pengguna non-staf ini untuk mengakses endpoint `/api/pengaduan/`
   - Dokumentasikan apa yang terjadi

4. **Ubah Permission Class**
   - Ubah `permission_classes` di `PengaduanViewSet` menjadi `IsAdminUser`:
   ```python
   from rest_framework.permissions import IsAdminUser
   
   class PengaduanViewSet(viewsets.ModelViewSet):
       queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
       serializer_class = PengaduanSerializer
       permission_classes = [IsAdminUser]
   ```

5. **Test Ulang**
   - Coba lagi akses `/api/pengaduan/` menggunakan token pengguna non-staf
   - Apa yang terjadi sekarang? (Seharusnya gagal dengan pesan **403 Forbidden**)
   - Coba juga dengan token superuser Anda (seharusnya berhasil dengan **200 OK**)

#### Hasil yang Diharapkan
- Memahami perbedaan antara `IsAuthenticated`, `IsAuthenticatedOrReadOnly`, dan `IsAdminUser`
- Pengalaman praktis dengan role-based access control
- Kemampuan untuk menguji berbagai skenario autentikasi

---

## Penutup & Preview

### Rangkuman
Selamat! API kita sekarang sudah aman. Kita telah membangun gerbang autentikasi dengan sistem token dan mengatur hak akses yang berbeda-beda menggunakan permission classes. Ini adalah langkah fundamental untuk membangun API yang siap produksi.

### Preview Pertemuan Berikutnya
API kita sekarang aman, tapi belum efisien untuk menangani data dalam jumlah besar. Bagaimana jika kita ingin mencari warga dengan nama tertentu, atau menampilkan ribuan data pengaduan dalam beberapa halaman agar tidak membebani klien? Di pertemuan selanjutnya, kita akan belajar cara mengimplementasikan fitur esensial: **Filtering, Searching, dan Pagination**.
