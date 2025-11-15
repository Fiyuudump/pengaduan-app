# Framework Programming - P12 Specification

## Topic: Profesionalitas: Dokumentasi API dengan Swagger/OpenAPI

### Overview
Mata Kuliah: Framework Programming  
Topik: Profesionalitas: Dokumentasi API dengan Swagger/OpenAPI  
Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:
- Menjelaskan mengapa dokumentasi API yang baik adalah hal yang krusial dalam pengembangan perangkat lunak tim
- Membedakan antara **OpenAPI Specification** dan **Swagger UI**
- Mengintegrasikan library `drf-spectacular` untuk menghasilkan skema OpenAPI secara otomatis
- Menghasilkan dan menyajikan halaman dokumentasi API yang interaktif (Swagger UI) dan statis (Redoc)
- Menggunakan antarmuka Swagger UI untuk memahami, menjelajahi, dan bahkan menguji endpoint API secara langsung

### Studi Kasus
Aplikasi kita sudah berfungsi penuh dari ujung ke ujung (backend hingga frontend sederhana). Bayangkan sekarang ada seorang developer baru yang bergabung dengan tim Anda untuk membuat aplikasi mobile. Pertanyaan pertama mereka pasti: "Bagaimana cara menggunakan API ini? Endpoint apa saja yang tersedia? Data apa yang harus saya kirim?"

Memberikan akses ke kode sumber saja tidak cukup. Kita perlu menyediakan sebuah "buku manual" atau "peta" untuk API kita. Dokumentasi adalah kontrak antara tim backend dan tim frontend (atau pengguna API lainnya).

---

## Section 3: Konsep Penting

### A. Mengapa Dokumentasi API Sangat Penting?

Sebuah API tanpa dokumentasi ibarat sebuah perangkat canggih tanpa buku panduan. Mungkin sangat kuat, tetapi tidak ada yang tahu cara menggunakannya.

**Dokumentasi yang baik berfungsi sebagai:**

1. **Sumber Kebenaran Tunggal**
   - Menjadi acuan resmi tentang cara kerja API
   - Mengurangi kesalahpahaman antar tim

2. **Alat Komunikasi Tim**
   - Memungkinkan tim backend dan frontend bekerja secara paralel
   - Tim frontend tidak perlu menunggu backend selesai untuk mengetahui struktur data yang akan mereka terima

3. **Mempercepat Onboarding**
   - Developer baru bisa langsung belajar dan produktif
   - Tidak perlu bertanya terus-menerus

4. **Memudahkan Pengujian**
   - Dokumentasi interaktif memungkinkan pengujian cepat
   - Tidak perlu membuka Postman setiap kali

### B. OpenAPI dan Swagger: Blueprint dan Bangunannya

Istilah ini sering digunakan secara bergantian, tetapi ada perbedaan penting:

#### 1. OpenAPI Specification
- **Standar** atau **aturan** tentang cara mendeskripsikan RESTful API
- Format: YAML atau JSON
- Analogi: Blueprint arsitektur sebuah gedung
- Mendefinisikan:
  - Path (URL)
  - Operasi (GET, POST, PUT, DELETE)
  - Parameter yang dibutuhkan
  - Skema data (request & response)
  - Authentication methods

#### 2. Swagger UI & Redoc
- **Tools** yang mengambil file spesifikasi OpenAPI dan merendernya
- Menghasilkan halaman web HTML yang indah dan interaktif
- Analogi: "Bangunan jadi" yang bisa kita jelajahi
- **Swagger UI**: Interaktif, bisa langsung testing
- **Redoc**: Lebih statis, tampilan bersih untuk dokumentasi

### C. drf-spectacular: Generator Blueprint Modern

**Apa itu drf-spectacular?**
- Library Django untuk generate OpenAPI 3 schema
- Memindai (introspect) kode kita secara otomatis:
  - Models
  - Views
  - Serializers
- Menghasilkan skema OpenAPI yang akurat tanpa menulis manual

**Keuntungan:**
- ✅ Automatic schema generation
- ✅ Support OpenAPI 3.0
- ✅ Highly customizable
- ✅ Support untuk authentication
- ✅ Support untuk filtering, searching, pagination
- ✅ Modern dan actively maintained

---

## Section 4: Sesi Praktikum (Sekitar 75 menit)

**Tujuan: Menghasilkan Halaman Dokumentasi Interaktif untuk API Kelurahan**

### Langkah 1: Instalasi drf-spectacular

1. **Pastikan virtual environment aktif**

2. **Install library:**
```bash
pip install drf-spectacular
```

3. **Daftarkan di `data_kelurahan/settings.py`:**
```python
# data_kelurahan/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'warga',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'drf_spectacular',  # Tambahkan ini
]
```

### Langkah 2: Konfigurasi Dasar

#### Update REST_FRAMEWORK Configuration

Buka `data_kelurahan/settings.py` dan tambahkan `DEFAULT_SCHEMA_CLASS`:

```python
# data_kelurahan/settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # Tambahkan konfigurasi schema class
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

#### Tambahkan SPECTACULAR_SETTINGS

Di bagian bawah `settings.py`, tambahkan:

```python
# data_kelurahan/settings.py
# ... existing settings ...

# DRF Spectacular Settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'API Aplikasi Warga Kelurahan',
    'DESCRIPTION': 'Dokumentasi API untuk mengelola data warga dan pengaduan. '
                   'API ini menyediakan endpoint untuk CRUD operations pada data warga dan pengaduan, '
                   'dengan fitur authentication, pagination, searching, dan filtering.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # Authentication configuration
    'SECURITY': [{'tokenAuth': []}],
    'COMPONENT_SPLIT_REQUEST': True,
    # Swagger UI settings
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
    },
}
```

### Langkah 3: Menambahkan URL untuk Dokumentasi

Kita perlu membuat endpoint di mana skema dan halaman UI dokumentasi bisa diakses.

#### Update `data_kelurahan/urls.py`:

```python
# data_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Import views dari drf-spectacular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),  # URL untuk web
    path('api/', include('warga.api_urls')),  # URL untuk API
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),  # P9: Token endpoint
    
    # --- P12: URL DOKUMENTASI API ---
    # Schema endpoint (menghasilkan file schema.yml)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # Swagger UI endpoint (dokumentasi interaktif)
    path('api/schema/swagger-ui/', 
         SpectacularSwaggerView.as_view(url_name='schema'), 
         name='swagger-ui'),
    
    # Redoc endpoint (dokumentasi alternatif)
    path('api/schema/redoc/', 
         SpectacularRedocView.as_view(url_name='schema'), 
         name='redoc'),
]
```

### Langkah 4: Update requirements.txt

Tambahkan dependency baru:

```bash
echo "drf-spectacular" >> requirements.txt
```

Atau manual edit `requirements.txt`:
```
asgiref==3.8.1
Django==5.2.7
django-cors-headers==4.6.0
django-filter==25.0
djangorestframework==3.16.1
drf-spectacular==0.28.0
pillow==11.2.1
sqlparse==0.5.3
```

### Langkah 5: Verifikasi Implementasi

1. **Jalankan server:**
```bash
python manage.py runserver
```

2. **Akses Swagger UI:**
   - URL: `http://127.0.0.1:8000/api/schema/swagger-ui/`
   - Anda akan melihat halaman dokumentasi yang profesional
   - Klik pada salah satu endpoint (misal: GET /api/warga/)
   - Lihat detailnya: parameters, response schema, dll.

3. **Akses Redoc:**
   - URL: `http://127.0.0.1:8000/api/schema/redoc/`
   - Tampilan dokumentasi yang lebih statis dan bersih
   - Cocok untuk print atau sharing

4. **Download Schema:**
   - URL: `http://127.0.0.1:8000/api/schema/`
   - Download file YAML schema
   - Bisa digunakan untuk code generation atau tools lain

### Langkah 6: Eksplorasi Swagger UI

**Fitur-fitur yang bisa dijelajahi:**

#### A. Endpoint List
- Semua endpoint terorganisir berdasarkan tag (Warga, Pengaduan)
- HTTP method ditampilkan dengan warna berbeda
- Deskripsi singkat untuk setiap endpoint

#### B. Endpoint Detail
Klik endpoint untuk melihat:
- **Parameters**: Query params (search, ordering, page)
- **Request Body**: Schema untuk POST/PUT
- **Responses**: Status codes dan schema response
- **Example Values**: Contoh request dan response

#### C. Authentication
- Klik tombol "Authorize" di kanan atas
- Masukkan token dengan format: `Token <your_token>`
- Semua request selanjutnya akan include token

#### D. Try It Out
- Klik "Try it out" pada endpoint
- Edit parameters atau request body
- Klik "Execute"
- Lihat response langsung dari server

---

## Section 5: Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

### Judul: Menggunakan Dokumentasi untuk Berinteraksi dengan API

Swagger UI bukan hanya untuk dibaca, tapi juga untuk dicoba. Gunakan halaman dokumentasi yang baru saja Anda buat untuk melakukan operasi POST (membuat data baru).

### Petunjuk:

#### 1. Dapatkan Token Authentication

**Via Swagger UI:**
1. Buka halaman Swagger UI: `http://127.0.0.1:8000/api/schema/swagger-ui/`
2. Cari endpoint `POST /api/auth/token/`
3. Klik "Try it out"
4. Edit request body dengan username dan password Anda:
   ```json
   {
     "username": "admin",
     "password": "admin123"
   }
   ```
5. Klik "Execute"
6. Copy token dari response

**Via curl:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

#### 2. Authorize di Swagger UI

1. Klik tombol **"Authorize"** di kanan atas halaman
2. Di field "tokenAuth (http, Token)", masukkan:
   ```
   Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
   ```
   (ganti dengan token Anda)
3. Klik "Authorize"
4. Klik "Close"

#### 3. Test POST Request untuk Membuat Pengaduan Baru

1. **Scroll ke endpoint `POST /api/pengaduan/`**

2. **Klik "Try it out"** (tombol hijau)

3. **Edit Request Body** dengan data pengaduan baru:
   ```json
   {
     "judul": "Lampu Jalan Mati di RT 05",
     "deskripsi": "Lampu jalan di Jl. Merdeka RT 05 sudah mati sejak 3 hari yang lalu. Mohon segera diperbaiki untuk keamanan warga.",
     "status": "BARU",
     "pelapor": 1
   }
   ```
   
   **Catatan:** 
   - `pelapor` harus ID warga yang valid
   - `status` pilihan: "BARU", "DIPROSES", "SELESAI"

4. **Klik "Execute"** (tombol biru)

5. **Periksa Response:**
   - **Code 201**: Berhasil! Pengaduan baru telah dibuat
   - **Code 400**: Ada error validasi, periksa pesan error
   - **Code 401**: Token tidak valid atau missing
   - **Code 403**: Permission denied

6. **Verifikasi Data:**
   - Scroll ke `GET /api/pengaduan/`
   - Klik "Try it out" → "Execute"
   - Pengaduan baru Anda harus muncul di list

#### 4. Test dengan Query Parameters

**Search:**
1. Buka `GET /api/pengaduan/`
2. Try it out
3. Isi parameter `search` dengan: `lampu`
4. Execute
5. Harus menampilkan pengaduan yang mengandung kata "lampu"

**Ordering:**
1. Isi parameter `ordering` dengan: `-tanggal_lapor`
2. Execute
3. Pengaduan terbaru harus muncul di atas

**Pagination:**
1. Isi parameter `page` dengan: `1`
2. Execute
3. Periksa response: `count`, `next`, `previous`

### Hasil yang Diharapkan

Setelah menyelesaikan tugas:
- ✅ Berhasil authenticate menggunakan token
- ✅ Berhasil create pengaduan baru via Swagger UI
- ✅ Memahami struktur request dan response
- ✅ Dapat menggunakan query parameters (search, ordering, page)
- ✅ Memahami HTTP status codes (200, 201, 400, 401, 403)
- ✅ Dapat verifikasi data yang baru dibuat

### Bonus Challenge (Opsional)

#### 1. Test Update (PUT/PATCH)
1. Buka `PUT /api/pengaduan/{id}/`
2. Pilih ID pengaduan yang ingin diupdate
3. Edit status menjadi "DIPROSES"
4. Execute dan verifikasi

#### 2. Test Delete
1. Buka `DELETE /api/pengaduan/{id}/`
2. Pilih ID pengaduan yang akan dihapus
3. Execute
4. Verifikasi dengan GET - data harus hilang

#### 3. Test dengan Warga Endpoint
1. Coba POST ke `/api/warga/` (tanpa token - harus 401)
2. Coba GET `/api/warga/` (tanpa token - harus sukses karena IsAuthenticatedOrReadOnly)
3. Pahami perbedaan permission class

---

## Section 6: Advanced Configuration (Optional)

### Menambahkan Deskripsi ke ViewSets

Untuk dokumentasi yang lebih baik, tambahkan docstrings ke ViewSets:

```python
# warga/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import WargaSerializer, PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    """
    ViewSet untuk mengelola data warga kelurahan.
    
    Endpoint ini menyediakan operasi CRUD lengkap untuk data warga.
    
    Permissions:
    - GET (list/detail): Public access (tidak perlu authentication)
    - POST/PUT/PATCH/DELETE: Memerlukan authentication token
    
    Features:
    - Pagination: 10 items per page
    - Search: Dapat mencari berdasarkan nama_lengkap, nik, atau alamat
    - Ordering: Dapat mengurutkan berdasarkan nama_lengkap atau tanggal_registrasi
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']

class PengaduanViewSet(viewsets.ModelViewSet):
    """
    ViewSet untuk mengelola data pengaduan warga.
    
    Endpoint ini menyediakan operasi CRUD lengkap untuk data pengaduan.
    
    Permissions:
    - Semua operasi memerlukan authentication token
    
    Features:
    - Pagination: 10 items per page
    - Search: Dapat mencari berdasarkan judul atau deskripsi
    - Ordering: Dapat mengurutkan berdasarkan status atau tanggal_lapor
    
    Status Options:
    - BARU: Pengaduan baru masuk
    - DIPROSES: Sedang ditangani
    - SELESAI: Pengaduan selesai ditangani
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']
```

### Menambahkan Examples ke Serializers

```python
# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan
from drf_spectacular.utils import extend_schema_field

class WargaSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Warga.
    
    Example:
        {
            "id": 1,
            "nik": "3501234567890001",
            "nama_lengkap": "Budi Santoso",
            "alamat": "Jl. Merdeka No. 10, RT 01/RW 02",
            "no_telepon": "081234567890"
        }
    """
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Pengaduan.
    
    Example:
        {
            "id": 1,
            "judul": "Lampu Jalan Mati",
            "deskripsi": "Lampu jalan di RT 05 mati",
            "status": "BARU",
            "tanggal_lapor": "2025-11-12T10:30:00Z",
            "pelapor": 1,
            "pelapor_nama": "Budi Santoso"
        }
    """
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)

    class Meta:
        model = Pengaduan
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor', 'pelapor_nama']
```

---

## Penutup & Preview

### Rangkuman
Selamat! Anda telah mencapai tahap akhir dari pengembangan backend profesional. Aplikasi Anda sekarang tidak hanya:
- ✅ Fungsional (CRUD lengkap)
- ✅ Aman (Authentication & Permissions)
- ✅ Efisien (Pagination, Filtering, Searching)
- ✅ Terintegrasi (Frontend JavaScript)
- ✅ **Terdokumentasi dengan baik** (Swagger/OpenAPI)

API Anda sekarang **production-ready** dan siap untuk:
- Dikonsumsi oleh developer lain
- Dikembangkan lebih lanjut
- Diintegrasikan dengan berbagai platform (web, mobile, desktop)
- Dipelihara dengan mudah

### Yang Telah Dipelajari

**Konsep:**
- Pentingnya dokumentasi API dalam tim development
- Perbedaan OpenAPI Specification vs Swagger UI
- Automatic schema generation dengan drf-spectacular

**Implementasi:**
- Install dan konfigurasi drf-spectacular
- Generate OpenAPI 3.0 schema
- Setup Swagger UI dan Redoc
- Customize documentation dengan docstrings
- Test API langsung via Swagger UI

**Best Practices:**
- Dokumentasi sebagai kontrak tim
- Interactive documentation untuk testing
- Versioning API
- Comprehensive endpoint descriptions

### Preview
Kita telah menyelesaikan semua materi inti dari mata kuliah Framework Programming:

1. ✅ **P1-P4**: Django Fundamentals (CBV, Models, Forms, CRUD)
2. ✅ **P5-P7**: API Development (DRF, Serializers, ViewSets, Routers)
3. ✅ **P9**: Authentication & Permissions
4. ✅ **P10**: Filtering, Searching, Pagination
5. ✅ **P11**: Frontend Integration (JavaScript fetch API, CORS)
6. ✅ **P12**: API Documentation (Swagger/OpenAPI)

**Pertemuan selanjutnya** akan digunakan untuk:
- Review komprehensif semua materi
- Sesi tanya jawab mendalam
- Troubleshooting dan best practices
- Persiapan **Proyek Akhir (UAS)**

Anda akan membangun sebuah API baru dari awal hingga akhir, menerapkan semua yang telah dipelajari!
