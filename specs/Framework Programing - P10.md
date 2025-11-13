# Framework Programming - P10 Specification

## Topic: Fitur Esensial: Filtering, Searching, & Pagination

### Overview
Mata Kuliah: Framework Programming  
Topik: Fitur Esensial: Filtering, Searching, & Pagination  
Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:
- Menjelaskan mengapa menampilkan ribuan data sekaligus dalam satu respons API adalah praktik yang buruk
- Mengimplementasikan **Pagination** secara global untuk membagi respons API menjadi halaman-halaman yang lebih kecil
- Mengimplementasikan **Searching** (SearchFilter) untuk memungkinkan klien mencari data berdasarkan kata kunci pada field teks
- Mengimplementasikan **Ordering** (OrderingFilter) untuk memungkinkan klien mengurutkan data berdasarkan field tertentu
- Menggunakan query parameters di URL (seperti `?page=2`, `?search=budi`, `?ordering=nama_lengkap`) untuk berinteraksi dengan fitur-fitur ini

### Studi Kasus
API kita sekarang sudah fungsional dan aman. Namun, bayangkan jika kelurahan kita memiliki ribuan warga dan puluhan ribu catatan pengaduan. Apa yang akan terjadi?

1. **Masalah Performa:** Mengakses `/api/warga/` akan mencoba mengambil ribuan data dari database dan mengirimkannya dalam satu respons JSON raksasa. Ini akan sangat lambat dan membebani server serta klien.
2. **Masalah Kegunaan:** Pengguna aplikasi (klien) akan kesulitan menemukan data spesifik. Bagaimana cara mencari warga yang bernama "Budi Santoso" di antara 5.000 warga lainnya?

Kita perlu membuat API kita lebih "pintar" dan efisien. Kita tidak akan mengirim semua data sekaligus, melainkan dalam potongan-potongan kecil (Pagination). Kita juga akan menyediakan "mesin pencari" agar klien bisa meminta data yang mereka butuhkan saja (Searching & Filtering).

---

## Section 4: Sesi Praktikum (Sekitar 75 menit)

**Tujuan: Membuat API Kelurahan Lebih Cepat dan Mudah Digunakan**

### Langkah 1: Menginstal django-filter

DRF memerlukan library ini untuk fungsionalitas filtering.

1. Pastikan virtual environment aktif
2. Install library:
```bash
pip install django-filter
```
3. Daftarkan di `data_kelurahan/settings.py`:
```python
# data_kelurahan/settings.py
INSTALLED_APPS = [
    # ...
    'warga',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',  # Tambahkan ini
]
```

### Langkah 2: Mengkonfigurasi Pagination Secara Global

Cara termudah adalah mengaktifkannya untuk seluruh proyek.

1. Buka `data_kelurahan/settings.py`
2. Modifikasi konfigurasi `REST_FRAMEWORK` yang sudah ada:
```python
# data_kelurahan/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # Tambahkan konfigurasi di bawah ini
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Jumlah item per halaman
}
```

3. **Verifikasi:** Jalankan server dan akses `http://127.0.0.1:8000/api/warga/` (dengan token jika diperlukan). Perhatikan struktur responsnya sekarang! Data Anda ada di dalam kunci `results`, dan ada `count`, `next`, serta `previous`.

### Langkah 3: Mengimplementasikan Searching dan Ordering pada WargaViewSet

1. Buka `warga/views.py`
2. Impor filter backend yang dibutuhkan
3. Tambahkan `filter_backends`, `search_fields`, dan `ordering_fields` ke dalam `WargaViewSet`:

```python
# warga/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter  # Impor ini
from .serializers import WargaSerializer
from .models import Warga

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # --- Tambahkan konfigurasi di bawah ini ---
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

# ... (PengaduanViewSet) ...
```

### Langkah 4: Verifikasi Fitur Baru

#### 1. Test Pagination
- Buka `http://127.0.0.1:8000/api/warga/` di browser
- Di Browsable API, Anda sekarang akan melihat tombol "Filters"
- Struktur response sekarang memiliki:
  - `count`: Total jumlah item
  - `next`: URL untuk halaman berikutnya
  - `previous`: URL untuk halaman sebelumnya
  - `results`: Daftar item untuk halaman saat ini

#### 2. Test Searching
- Uji Pencarian: Coba akses `http://127.0.0.1:8000/api/warga/?search=Budi`
- Ganti "Budi" dengan bagian dari nama warga yang ada di data Anda
- API akan mencari di field `nama_lengkap`, `nik`, dan `alamat`

#### 3. Test Ordering
- Urutkan A-Z: `http://127.0.0.1:8000/api/warga/?ordering=nama_lengkap`
- Urutkan Z-A: `http://127.0.0.1:8000/api/warga/?ordering=-nama_lengkap`
- Urutkan berdasarkan tanggal registrasi (terbaru): `http://127.0.0.1:8000/api/warga/?ordering=-tanggal_registrasi`

#### 4. Kombinasi Query Parameters
Anda bisa mengkombinasikan berbagai parameter:
```
http://127.0.0.1:8000/api/warga/?search=Budi&ordering=nama_lengkap&page=1
```

---

## Section 5: Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

### Judul: Menerapkan Fitur Serupa pada API Pengaduan

API Warga kita sekarang sudah canggih. Terapkan fungsionalitas yang sama pada `PengaduanViewSet`.

#### Petunjuk:

1. **Buka File Views**
   - Buka `warga/views.py`

2. **Tambahkan Filter Backends ke PengaduanViewSet**
   ```python
   # warga/views.py
   from rest_framework import viewsets
   from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
   from rest_framework.filters import SearchFilter, OrderingFilter
   from .serializers import WargaSerializer, PengaduanSerializer
   from .models import Warga, Pengaduan

   class WargaViewSet(viewsets.ModelViewSet):
       queryset = Warga.objects.all().order_by('-tanggal_registrasi')
       serializer_class = WargaSerializer
       permission_classes = [IsAuthenticatedOrReadOnly]
       filter_backends = [SearchFilter, OrderingFilter]
       search_fields = ['nama_lengkap', 'nik', 'alamat']
       ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

   class PengaduanViewSet(viewsets.ModelViewSet):
       queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
       serializer_class = PengaduanSerializer
       permission_classes = [IsAuthenticated]
       
       # Tambahkan konfigurasi di bawah ini
       filter_backends = [SearchFilter, OrderingFilter]
       search_fields = ['judul', 'deskripsi']  # Field untuk pencarian
       ordering_fields = ['status', 'tanggal_lapor']  # Field untuk pengurutan
   ```

3. **Test Fitur pada Endpoint Pengaduan**
   
   Gunakan Postman atau browser (jangan lupa token jika diperlukan):
   
   - **Test Pagination:**
     ```
     GET http://127.0.0.1:8000/api/pengaduan/
     ```
     Periksa struktur response (count, next, previous, results)
   
   - **Test Searching:**
     ```
     GET http://127.0.0.1:8000/api/pengaduan/?search=rusak
     ```
     Cari pengaduan yang memiliki kata "rusak" di judul atau deskripsi
   
   - **Test Ordering:**
     ```
     GET http://127.0.0.1:8000/api/pengaduan/?ordering=status
     GET http://127.0.0.1:8000/api/pengaduan/?ordering=-tanggal_lapor
     ```
     Urutkan berdasarkan status atau tanggal lapor
   
   - **Test Kombinasi:**
     ```
     GET http://127.0.0.1:8000/api/pengaduan/?search=jalan&ordering=-tanggal_lapor&page=1
     ```

4. **Dokumentasikan Hasil**
   
   Catat hasil testing Anda:
   - Berapa jumlah item per halaman?
   - Apakah pencarian berhasil menemukan data yang relevan?
   - Apakah pengurutan berfungsi dengan benar (ascending dan descending)?
   - Screenshot hasil dari Postman atau browser

#### Hasil yang Diharapkan
- Pagination bekerja dengan baik pada endpoint `/api/pengaduan/`
- Searching berhasil mencari text di field `judul` dan `deskripsi`
- Ordering berhasil mengurutkan berdasarkan `status` dan `tanggal_lapor`
- Pemahaman tentang cara mengkombinasikan query parameters

#### Bonus Challenge (Opsional)
Coba tambahkan field filtering yang lebih spesifik:
```python
from django_filters.rest_framework import DjangoFilterBackend

class PengaduanViewSet(viewsets.ModelViewSet):
    # ... existing code ...
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'warga']  # Filter exact match
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']
```

Kemudian test:
```
GET http://127.0.0.1:8000/api/pengaduan/?status=pending
GET http://127.0.0.1:8000/api/pengaduan/?warga=1
```

---

## Penutup & Preview

### Rangkuman
Selamat! API kita tidak hanya fungsional dan aman, tetapi sekarang juga efisien dan mudah digunakan. Dengan Pagination, Searching, dan Ordering, kita telah membangun API yang mampu menangani data dalam skala besar, sebuah ciri khas dari aplikasi profesional.

### Fitur yang Telah Diimplementasikan
✅ Pagination - Membagi data menjadi halaman-halaman kecil  
✅ Searching - Mencari data berdasarkan kata kunci  
✅ Ordering - Mengurutkan data secara ascending/descending  
✅ Query Parameters - Mengontrol API dengan URL parameters  

### Preview Pertemuan Berikutnya
Kita telah menghabiskan banyak waktu membangun "mesin" backend yang sangat kuat. Di pertemuan selanjutnya, kita akan mengalami momen "Aha!" yang paling ditunggu-tunggu. Kita akan membuat halaman web sederhana menggunakan HTML dan **JavaScript (fetch API)** untuk **mengkonsumsi** atau menggunakan data dari API yang telah kita bangun. Inilah saatnya kita melihat bagaimana backend dan frontend akhirnya bertemu.
