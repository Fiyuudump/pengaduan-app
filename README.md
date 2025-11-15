# Aplikasi Warga Kelurahan

Sistem informasi sederhana untuk mengelola data warga dan pengumuman di lingkungan kelurahan yang dibangun menggunakan Django framework.

## Implementasi Spesifikasi

### ✅ P1 - Fondasi Django & Migrasi ke Class-Based Views (CBV)
- [x] Setup proyek Django `data_kelurahan`
- [x] Membuat aplikasi `warga`
- [x] Model `Warga` dengan fields: NIK, nama_lengkap, alamat, no_telepon, tanggal_registrasi
- [x] `WargaListView` (ListView) untuk menampilkan daftar warga
- [x] `WargaDetailView` (DetailView) untuk menampilkan detail warga
- [x] Template `warga_list.html` dan `warga_detail.html`
- [x] URL configuration dan admin registration

### ✅ P2 - Relasi Model & QuerySet Lanjutan
- [x] Model `Pengaduan` dengan relasi ForeignKey ke `Warga`
- [x] Fields: judul, deskripsi, status (choices), tanggal_lapor, pelapor
- [x] Update template `warga_detail.html` untuk menampilkan daftar pengaduan
- [x] `PengaduanListView` (Challenge) untuk menampilkan semua pengaduan
- [x] Template `pengaduan_list.html`
- [x] Admin registration untuk model `Pengaduan`

### ✅ P3 - Interaksi Pengguna dengan Django Forms & CreateView
- [x] `WargaForm` menggunakan ModelForm untuk form input warga
- [x] `WargaCreateView` untuk menambahkan warga baru
- [x] Template `warga_form.html` dengan CSRF token dan form rendering
- [x] URL configuration untuk form tambah warga (`/tambah/`)
- [x] Link "Tambah Warga Baru" di halaman list
- [x] `PengaduanForm` dan `PengaduanCreateView` (Challenge)
- [x] Template `pengaduan_form.html` dan URL `/pengaduan/tambah/`
- [x] success_url menggunakan reverse_lazy

### ✅ P4 - Melengkapi CRUD dengan UpdateView & DeleteView
- [x] `WargaUpdateView` untuk mengedit data warga (menggunakan template yang sama)
- [x] `WargaDeleteView` dengan halaman konfirmasi
- [x] Template `warga_confirm_delete.html` dengan konfirmasi hapus
- [x] URL patterns untuk edit (`/<pk>/edit/`) dan hapus (`/<pk>/hapus/`)
- [x] Link "Edit Data" dan "Hapus Data" di halaman detail warga
- [x] `PengaduanUpdateView` dan `PengaduanDeleteView` (Challenge)
- [x] Template `pengaduan_confirm_delete.html`
- [x] Link Edit dan Hapus di halaman daftar pengaduan
- [x] Complete CRUD cycle untuk kedua model

### ✅ P5 - Konsep Fundamental API & Dunia JSON
- [x] Pemahaman arsitektur Monolitik vs Decoupled (Headless)
- [x] Konsep API sebagai Application Programming Interface
- [x] Prinsip REST (Representational State Transfer)
- [x] Format JSON sebagai bahasa universal API
- [x] Praktikum dengan API publik (reqres.in) menggunakan tools seperti Postman
- [x] Understanding HTTP methods (GET, POST, PUT, DELETE)
- [x] Status codes (200 OK, 201 Created, 404 Not Found)
- [x] Dokumentasi konsep API dalam file `P5_API_Concepts.md`

### ✅ P6 - Hello, API! Pengenalan Django REST Framework (DRF)
- [x] Instalasi dan konfigurasi Django REST Framework
- [x] `WargaSerializer` menggunakan ModelSerializer
- [x] `WargaListAPIView` menggunakan ListAPIView untuk endpoint list
- [x] `WargaDetailAPIView` menggunakan RetrieveAPIView (Challenge)
- [x] `PengaduanSerializer` dengan relasi pelapor_nama (read_only)
- [x] `PengaduanListAPIView` dan `PengaduanDetailAPIView` untuk API pengaduan
- [x] File `serializers.py` untuk data serialization
- [x] File `api_urls.py` untuk API URL configuration
- [x] Browsable API interface untuk testing dan debugging
- [x] Complete API endpoints untuk kedua model (Warga & Pengaduan)
- [x] Navigation links antar halaman untuk user experience

### ✅ P7 - ViewSets & Routers: Menyederhanakan Arsitektur API
- [x] Refactoring dari APIView ke ViewSet architecture
- [x] `WargaViewSet` menggunakan ModelViewSet untuk operasi CRUD lengkap
- [x] `PengaduanViewSet` menggunakan ModelViewSet
- [x] Implementasi Router untuk automatic URL routing
- [x] Single endpoint untuk multiple operations (list, create, retrieve, update, delete)
- [x] Reduced code complexity dengan ViewSet pattern
- [x] RESTful URL structure dengan Router

### ✅ P9 - Mengamankan API dengan Autentikasi & Permissions
- [x] Token Authentication implementation untuk API security
- [x] `rest_framework.authtoken` app configuration
- [x] Token endpoint `/api/auth/token/` untuk mendapatkan auth token
- [x] Global authentication dan permission classes configuration
- [x] `IsAuthenticatedOrReadOnly` permission untuk WargaViewSet
- [x] `IsAuthenticated` permission untuk PengaduanViewSet
- [x] Token-based authentication untuk protected endpoints
- [x] Role-based access control (public read vs authenticated write)
- [x] Security best practices untuk production-ready API

### ✅ P10 - Fitur Esensial: Filtering, Searching, & Pagination
- [x] Django-filter package installation dan configuration
- [x] Global pagination dengan PageNumberPagination
- [x] PAGE_SIZE configuration (10 items per page)
- [x] SearchFilter implementation untuk full-text search
- [x] OrderingFilter untuk dynamic data sorting
- [x] WargaViewSet: search by nama_lengkap, nik, alamat
- [x] WargaViewSet: ordering by nama_lengkap, tanggal_registrasi
- [x] PengaduanViewSet: search by judul, deskripsi
- [x] PengaduanViewSet: ordering by status, tanggal_lapor
- [x] Query parameters support (?search=, ?ordering=, ?page=)
- [x] Paginated API responses dengan count, next, previous links

### ✅ P11 - Konsumsi API dengan Frontend JavaScript & CORS
- [x] Django-cors-headers package installation
- [x] CORS middleware configuration untuk cross-origin requests
- [x] CORS_ALLOW_ALL_ORIGINS untuk development environment
- [x] Separate frontend folder (`view_kelurahan/`) di luar proyek Django
- [x] HTML/CSS frontend dengan modern styling
- [x] JavaScript fetch API untuk HTTP requests
- [x] Dynamic DOM manipulation untuk rendering data
- [x] Pagination UI dengan prev/next navigation
- [x] Search functionality dengan real-time filtering
- [x] Error handling dan connection status monitoring
- [x] Decoupled architecture (frontend ↔ backend separation)
- [x] Browser-based API consumption tanpa Django templates

### ✅ P12 - Dokumentasi API Profesional dengan Swagger/OpenAPI
- [x] drf-spectacular package installation
- [x] OpenAPI 3.0 schema generation otomatis
- [x] DEFAULT_SCHEMA_CLASS configuration di REST_FRAMEWORK
- [x] SPECTACULAR_SETTINGS untuk customization
- [x] Swagger UI endpoint (`/api/schema/swagger-ui/`) untuk interactive docs
- [x] Redoc endpoint (`/api/schema/redoc/`) untuk alternative documentation
- [x] Schema endpoint (`/api/schema/`) untuk raw OpenAPI schema
- [x] Enhanced ViewSet docstrings untuk detailed API descriptions
- [x] Token authentication integration dalam dokumentasi
- [x] Interactive API testing langsung dari browser
- [x] Professional API documentation untuk tim development

## Struktur Proyek

```
data_kelurahan/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── populate_data.py
├── data_kelurahan/
│   ├── __init__.py
│   ├── settings.py          # P9 & P10: REST_FRAMEWORK configuration
│   │                        # P11: CORS configuration
│   │                        # P12: SPECTACULAR_SETTINGS
│   ├── urls.py               # P9: Token auth endpoint
│   │                        # P12: Documentation endpoints
│   └── wsgi.py
├── warga/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py              # P9 & P10: ViewSets with permissions & filters
│   │                        # P12: Enhanced docstrings for API docs
│   ├── serializers.py
│   ├── urls.py
│   ├── api_urls.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/
│       └── warga/
│           ├── warga_list.html
│           ├── warga_detail.html
│           ├── warga_form.html
│           ├── warga_confirm_delete.html
│           ├── pengaduan_list.html
│           ├── pengaduan_form.html
│           └── pengaduan_confirm_delete.html
└── view_kelurahan/          # P11: Frontend folder (separate from Django)
    ├── index.html           # Main HTML page with modern styling
    └── app.js               # JavaScript for API consumption
```

## Cara Menjalankan

1. **Aktivasi Virtual Environment:**
   ```bash
   source myenv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Migrasi Database:**
   ```bash
   python manage.py migrate
   ```

4. **Populate Data (Opsional):**
   ```bash
   python populate_data.py
   ```

5. **Membuat Superuser (Untuk API Authentication):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Menjalankan Server:**
   ```bash
   python manage.py runserver
   ```

7. **Mendapatkan Token Authentication (P9):**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/auth/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
   ```
   
   Atau gunakan Postman:
   - Method: POST
   - URL: `http://127.0.0.1:8000/api/auth/token/`
   - Body (JSON): `{"username": "your_username", "password": "your_password"}`
   - Response akan berisi token yang perlu disimpan

## URL Endpoints

### Warga URLs
- `/warga/` - Daftar semua warga (WargaListView)
- `/warga/tambah/` - Form tambah warga baru (WargaCreateView)
- `/warga/<id>/` - Detail warga beserta daftar pengaduannya (WargaDetailView)  
- `/warga/<id>/edit/` - Form edit warga (WargaUpdateView)
- `/warga/<id>/hapus/` - Konfirmasi hapus warga (WargaDeleteView)

### Pengaduan URLs
- `/warga/pengaduan/` - Daftar semua pengaduan (PengaduanListView)
- `/warga/pengaduan/tambah/` - Form tambah pengaduan baru (PengaduanCreateView)
- `/warga/pengaduan/<id>/edit/` - Form edit pengaduan (PengaduanUpdateView)
- `/warga/pengaduan/<id>/hapus/` - Konfirmasi hapus pengaduan (PengaduanDeleteView)

### API Endpoints (JSON)
- `/api/warga/` - List semua warga dalam format JSON (WargaListAPIView)
- `/api/warga/<id>/` - Detail warga spesifik dalam format JSON (WargaDetailAPIView)
- `/api/pengaduan/` - List semua pengaduan dalam format JSON (PengaduanListAPIView)
- `/api/pengaduan/<id>/` - Detail pengaduan spesifik dalam format JSON (PengaduanDetailAPIView)

### API Authentication & Security (P9)
- `/api/auth/token/` - **POST** endpoint untuk mendapatkan authentication token
  - Request Body: `{"username": "your_username", "password": "your_password"}`
  - Response: `{"token": "your_auth_token_here"}`
  - Token harus disertakan dalam header untuk protected endpoints

### API Documentation (P12)
- `/api/schema/` - OpenAPI 3.0 schema (YAML format)
- `/api/schema/swagger-ui/` - Interactive API documentation (Swagger UI)
- `/api/schema/redoc/` - Alternative API documentation (Redoc)

### API Query Parameters (P10)
Semua list endpoints mendukung query parameters berikut:

#### Pagination
- `?page=<number>` - Navigasi ke halaman tertentu
- Contoh: `/api/warga/?page=2`
- Response includes: `count`, `next`, `previous`, `results`

#### Searching (WargaViewSet)
- `?search=<keyword>` - Cari di fields: nama_lengkap, nik, alamat
- Contoh: `/api/warga/?search=Budi`
- Contoh: `/api/warga/?search=3501234567890001`

#### Searching (PengaduanViewSet)
- `?search=<keyword>` - Cari di fields: judul, deskripsi
- Contoh: `/api/pengaduan/?search=jalan`
- Contoh: `/api/pengaduan/?search=rusak`

#### Ordering (WargaViewSet)
- `?ordering=<field>` - Urutkan ascending
- `?ordering=-<field>` - Urutkan descending
- Fields: `nama_lengkap`, `tanggal_registrasi`
- Contoh: `/api/warga/?ordering=nama_lengkap` (A-Z)
- Contoh: `/api/warga/?ordering=-tanggal_registrasi` (terbaru dulu)

#### Ordering (PengaduanViewSet)
- `?ordering=<field>` - Urutkan ascending
- `?ordering=-<field>` - Urutkan descending
- Fields: `status`, `tanggal_lapor`
- Contoh: `/api/pengaduan/?ordering=status`
- Contoh: `/api/pengaduan/?ordering=-tanggal_lapor`

#### Kombinasi Query Parameters
Query parameters dapat dikombinasikan:
- `/api/warga/?search=Budi&ordering=nama_lengkap&page=1`
- `/api/pengaduan/?search=jalan&ordering=-tanggal_lapor&page=1`

### Admin
- `/admin/` - Interface admin Django

## Models

### Warga
- `nik`: CharField(16) - Nomor Induk Kependudukan (unique)
- `nama_lengkap`: CharField(100) - Nama Lengkap
- `alamat`: TextField - Alamat Tinggal
- `no_telepon`: CharField(15) - Nomor Telepon (optional)
- `tanggal_registrasi`: DateTimeField - Tanggal Registrasi (auto)

### Pengaduan  
- `judul`: CharField(200) - Judul Pengaduan
- `deskripsi`: TextField - Deskripsi Pengaduan
- `status`: CharField(10) - Status (BARU/DIPROSES/SELESAI)
- `tanggal_lapor`: DateTimeField - Tanggal Lapor (auto)
- `pelapor`: ForeignKey(Warga) - Relasi ke Warga

## Fitur

### Class-Based Views (CBV)
- Menggunakan generic CBV (ListView, DetailView) untuk efisiensi kode
- Template naming convention otomatis Django
- Reusable dan mudah dikustomisasi

### Relasi Database
- One-to-Many relationship antara Warga dan Pengaduan
- QuerySet API untuk mengakses data terkait
- Related manager (`warga.pengaduan.all()`)

### Django Forms & CRUD Operations
- ModelForm untuk otomatis generate form dari model
- CSRF protection untuk keamanan form
- CreateView, UpdateView, DeleteView untuk operasi CRUD lengkap
- Form validation dan error handling
- Success URL redirect setelah operasi berhasil
- Confirmation pages untuk delete operations

### API Development dengan Django REST Framework
- REST API architecture dengan JSON response
- ModelSerializer untuk data serialization/deserialization
- ViewSets untuk full CRUD operations dengan single class
- Router untuk automatic URL routing
- Browsable API untuk testing dan debugging
- Separation of API URLs dari web URLs
- HTTP status codes dan RESTful principles

### API Security & Authentication (P9)
- **Token Authentication** untuk mengamankan API endpoints
- Token generation endpoint untuk user login
- **Permission Classes** untuk access control:
  - `IsAuthenticatedOrReadOnly`: Public dapat read, authenticated dapat write
  - `IsAuthenticated`: Hanya authenticated users yang dapat akses
- Role-based access control (RBAC)
- Header-based authentication dengan format: `Authorization: Token <your_token>`
- Secure API endpoints sesuai business logic

### API Advanced Features (P10)
- **Pagination**: Automatic response pagination dengan 10 items per page
  - Response structure: `count`, `next`, `previous`, `results`
  - Page navigation dengan query parameter `?page=<number>`
- **Searching**: Full-text search dengan SearchFilter
  - Multiple field searching (nama_lengkap, nik, alamat untuk Warga)
  - Multiple field searching (judul, deskripsi untuk Pengaduan)
  - Query parameter: `?search=<keyword>`
- **Ordering**: Dynamic sorting dengan OrderingFilter
  - Ascending dan descending sort
  - Query parameters: `?ordering=<field>` atau `?ordering=-<field>`
- **Query Combination**: Multiple query parameters dapat dikombinasikan
- Performance optimization untuk large datasets

### Admin Interface
- Model registration untuk kemudahan pengelolaan data
- Interface bawaan Django untuk CRUD operations

## Status Implementasi

- ✅ **P1 (Framework Programming - Pertemuan 1)**: Completed
- ✅ **P2 (Framework Programming - Pertemuan 2)**: Completed
- ✅ **P3 (Framework Programming - Pertemuan 3)**: Completed
- ✅ **P4 (Framework Programming - Pertemuan 4)**: Completed
- ✅ **P5 (Framework Programming - Pertemuan 5)**: Completed
- ✅ **P6 (Framework Programming - Pertemuan 6)**: Completed
- ✅ **P7 (Framework Programming - Pertemuan 7)**: Completed
- ✅ **P9 (Framework Programming - Pertemuan 9)**: Completed - Authentication & Permissions
- ✅ **P10 (Framework Programming - Pertemuan 10)**: Completed - Filtering, Searching & Pagination
- ✅ **P11 (Framework Programming - Pertemuan 11)**: Completed - Frontend JavaScript & CORS
- ✅ **P12 (Framework Programming - Pertemuan 12)**: Completed - API Documentation with Swagger

## Penggunaan API dengan Authentication

### 1. Mendapatkan Token (Login)
```bash
# Menggunakan curl
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Response
{"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}
```

### 2. Mengakses Protected Endpoint
```bash
# Menggunakan token di header
curl -X GET http://127.0.0.1:8000/api/pengaduan/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"

# Tanpa token akan mendapat 401 Unauthorized
curl -X GET http://127.0.0.1:8000/api/pengaduan/
# Response: {"detail":"Authentication credentials were not provided."}
```

### 3. Public Read Access (Warga Endpoint)
```bash
# GET request tidak perlu token (IsAuthenticatedOrReadOnly)
curl -X GET http://127.0.0.1:8000/api/warga/

# Tapi POST/PUT/DELETE perlu token
curl -X POST http://127.0.0.1:8000/api/warga/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nik": "1234567890123456", "nama_lengkap": "Test User", "alamat": "Test Address"}'
```

### 4. Menggunakan Pagination
```bash
# Halaman pertama (default)
curl http://127.0.0.1:8000/api/warga/

# Response structure:
# {
#   "count": 25,
#   "next": "http://127.0.0.1:8000/api/warga/?page=2",
#   "previous": null,
#   "results": [...]
# }

# Halaman kedua
curl http://127.0.0.1:8000/api/warga/?page=2
```

### 5. Menggunakan Search
```bash
# Cari warga bernama "Budi"
curl "http://127.0.0.1:8000/api/warga/?search=Budi"

# Cari berdasarkan NIK
curl "http://127.0.0.1:8000/api/warga/?search=3501234567890001"

# Cari pengaduan dengan keyword "jalan"
curl -H "Authorization: Token YOUR_TOKEN" \
  "http://127.0.0.1:8000/api/pengaduan/?search=jalan"
```

### 6. Menggunakan Ordering
```bash
# Urutkan warga A-Z berdasarkan nama
curl "http://127.0.0.1:8000/api/warga/?ordering=nama_lengkap"

# Urutkan Z-A (descending)
curl "http://127.0.0.1:8000/api/warga/?ordering=-nama_lengkap"

# Urutkan berdasarkan tanggal registrasi (terbaru dulu)
curl "http://127.0.0.1:8000/api/warga/?ordering=-tanggal_registrasi"

# Urutkan pengaduan berdasarkan status
curl -H "Authorization: Token YOUR_TOKEN" \
  "http://127.0.0.1:8000/api/pengaduan/?ordering=status"
```

### 7. Kombinasi Query Parameters
```bash
# Search + Ordering
curl "http://127.0.0.1:8000/api/warga/?search=Siti&ordering=nama_lengkap"

# Search + Ordering + Pagination
curl "http://127.0.0.1:8000/api/warga/?search=Ahmad&ordering=-tanggal_registrasi&page=1"

# Dengan Authentication
curl -H "Authorization: Token YOUR_TOKEN" \
  "http://127.0.0.1:8000/api/pengaduan/?search=rusak&ordering=-tanggal_lapor&page=1"
```

### 8. Testing dengan Postman / Insomnia

#### Import Insomnia Collection (Recommended)
File: `Insomnia_P9_P10_API_Tests.yaml`

Collection ini berisi 24+ pre-configured requests untuk testing:
- ✅ P9: Authentication & Permissions (7 requests)
- ✅ P10: Pagination (2 requests)
- ✅ P10: Searching (5 requests)
- ✅ P10: Ordering (5 requests)
- ✅ P10: Combined Queries (2 requests)

**Cara Import:**
1. Buka Insomnia
2. Create → Import From → File
3. Pilih `Insomnia_P9_P10_API_Tests.yaml`
4. Edit Environment variables:
   - `base_url`: `http://127.0.0.1:8000`
   - `username`: your superuser username
   - `password`: your superuser password
5. Run "Get Authentication Token" request
6. Copy token dari response ke environment variable `auth_token`
7. Test semua endpoints!

#### Manual Testing dengan Postman:

**Mendapatkan Token:**
1. Method: `POST`
2. URL: `http://127.0.0.1:8000/api/auth/token/`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
   ```json
   {
     "username": "admin",
     "password": "admin123"
   }
   ```
5. Copy token dari response

**Menggunakan Token:**
1. Method: `GET` / `POST` / `PUT` / `DELETE`
2. URL: `http://127.0.0.1:8000/api/pengaduan/`
3. Headers Tab:
   - Key: `Authorization`
   - Value: `Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

**Query Parameters di Postman:**
1. Gunakan Params tab
2. Tambahkan key-value pairs:
   - `search`: `Budi`
   - `ordering`: `-tanggal_registrasi`
   - `page`: `1`

## Permission Levels

### WargaViewSet - IsAuthenticatedOrReadOnly
- ✅ **Public (No Token)**: GET (list & detail)
- ❌ **Public (No Token)**: POST, PUT, PATCH, DELETE → 401 Unauthorized
- ✅ **Authenticated**: All methods (GET, POST, PUT, PATCH, DELETE)

### PengaduanViewSet - IsAuthenticated
- ❌ **Public (No Token)**: All methods → 401 Unauthorized
- ✅ **Authenticated**: All methods (GET, POST, PUT, PATCH, DELETE)

## Teknologi

- **Framework**: Django 5.2.7
- **API Framework**: Django REST Framework 3.16.1
- **Database**: SQLite3
- **Python**: 3.13.7
- **Template Engine**: Django Templates
- **API Format**: JSON
- **Authentication**: Token Authentication (rest_framework.authtoken)
- **Filtering**: django-filter 25.0
- **CORS**: django-cors-headers 4.6.0
- **API Documentation**: drf-spectacular 0.28.0 (OpenAPI 3.0)
- **Frontend**: Vanilla JavaScript (Fetch API, DOM Manipulation)
- **Environment**: Virtual Environment (myenv)

## Best Practices Implemented

### Security (P9)
- ✅ Token-based authentication untuk stateless API
- ✅ Role-based access control dengan permission classes
- ✅ Protected endpoints untuk sensitive data
- ✅ Separation of public dan private endpoints

### Performance (P10)
- ✅ Pagination untuk efficient data loading
- ✅ Query optimization dengan filtering
- ✅ Database indexing pada search fields
- ✅ Reduced response size dengan pagination

### API Design
- ✅ RESTful URL structure
- ✅ Proper HTTP methods dan status codes
- ✅ Consistent error responses
- ✅ Browsable API untuk documentation
- ✅ Query parameters untuk flexible data retrieval

## Troubleshooting

### Token Authentication Issues
- **401 Unauthorized**: Pastikan token valid dan format header benar
  ```
  Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
  ```
- **Token tidak ada**: Buat superuser dan request token via `/api/auth/token/`

### Pagination Issues
- Response tidak ter-paginate: Periksa `REST_FRAMEWORK` configuration di `settings.py`
- PAGE_SIZE terlalu kecil/besar: Sesuaikan nilai `PAGE_SIZE` di settings

### Search/Filter Issues
- Search tidak bekerja: Pastikan `django-filter` terinstall dan ada di `INSTALLED_APPS`
- Field tidak searchable: Tambahkan field ke `search_fields` di ViewSet

### Migration Issues
- Jika ada error saat migrate: Hapus `db.sqlite3` dan jalankan ulang `python manage.py migrate`
- Token table tidak ada: Pastikan `rest_framework.authtoken` ada di `INSTALLED_APPS`

## P11: Frontend JavaScript Integration

### Menjalankan Frontend
1. **Pastikan Django server berjalan:**
   ```bash
   python manage.py runserver
   ```

2. **Buka frontend di browser:**
   ```bash
   # Dari folder view_kelurahan
   cd view_kelurahan
   
   # Buka index.html di browser (double-click atau)
   # Linux/Mac:
   xdg-open index.html
   # Atau langsung buka file://path/to/view_kelurahan/index.html di browser
   ```

3. **Frontend akan otomatis:**
   - Connect ke API Django di `http://127.0.0.1:8000/api/warga/`
   - Menampilkan daftar warga dengan pagination
   - Menampilkan status koneksi (✅ Connected atau ❌ Failed)
   - Menyediakan search functionality

### Fitur Frontend
- ✅ **Fetch API**: Modern JavaScript HTTP requests
- ✅ **Dynamic Rendering**: DOM manipulation untuk display data
- ✅ **Pagination**: Navigasi prev/next dengan page counter
- ✅ **Search**: Real-time search dengan reset button
- ✅ **Error Handling**: User-friendly error messages
- ✅ **Connection Status**: Visual indicator koneksi ke API
- ✅ **Responsive Design**: Modern CSS dengan hover effects

### Troubleshooting Frontend

#### CORS Error di Browser Console
```
Access to fetch at 'http://127.0.0.1:8000/api/warga/' from origin 'null' has been blocked by CORS policy
```

**Solusi:**
1. Pastikan `corsheaders` ada di `INSTALLED_APPS`
2. Pastikan `CorsMiddleware` ada di `MIDDLEWARE` (paling atas)
3. Pastikan `CORS_ALLOW_ALL_ORIGINS = True` ada di `settings.py`

#### Data Tidak Muncul
1. Cek browser console (F12) untuk error messages
2. Pastikan Django server berjalan di port 8000
3. Pastikan API endpoint accessible: `http://127.0.0.1:8000/api/warga/`
4. Cek connection status di halaman frontend

#### Pagination Tidak Muncul
- Pastikan ada data warga di database (minimal 11 item untuk 2 halaman)
- Jalankan `python populate_data.py` untuk generate test data

### Arsitektur Decoupled
Frontend (`view_kelurahan/`) dan Backend (`data_kelurahan/`) adalah **proyek terpisah**:
- ✅ Frontend: Static HTML/JS files, bisa di-host di mana saja
- ✅ Backend: Django API server, pure JSON responses
- ✅ Communication: HTTP requests via fetch API
- ✅ CORS: Mengizinkan cross-origin requests dari frontend

## P12: API Documentation dengan Swagger

### Mengakses Dokumentasi API

#### 1. Swagger UI (Interactive Documentation)
**URL**: `http://127.0.0.1:8000/api/schema/swagger-ui/`

Fitur:
- ✅ Interactive API testing langsung dari browser
- ✅ Try-it-out functionality untuk setiap endpoint
- ✅ Token authentication support
- ✅ Request/response examples
- ✅ Schema definitions untuk setiap model

**Cara Menggunakan:**
1. Buka URL di browser
2. Klik "Authorize" button di kanan atas
3. Masukkan token dengan format: `Token YOUR_TOKEN_HERE`
4. Klik "Authorize" untuk simpan token
5. Sekarang bisa test semua endpoint yang requires authentication
6. Klik endpoint → "Try it out" → Fill parameters → "Execute"

#### 2. Redoc (Alternative Documentation)
**URL**: `http://127.0.0.1:8000/api/schema/redoc/`

Fitur:
- ✅ Clean, professional documentation view
- ✅ Better for reading dan sharing
- ✅ Three-panel layout (navigation, content, examples)
- ✅ Print-friendly format
- ✅ Cocok untuk onboarding developer baru

#### 3. OpenAPI Schema (Raw)
**URL**: `http://127.0.0.1:8000/api/schema/`

- Download raw OpenAPI 3.0 schema dalam format YAML
- Bisa digunakan untuk generate client libraries
- Compatible dengan tools seperti Postman, Insomnia, dll

### Enhanced API Documentation Features

#### ViewSet Docstrings
Setiap ViewSet memiliki comprehensive docstring yang menjelaskan:
- ✅ Tujuan endpoint
- ✅ Authentication requirements
- ✅ Query parameters yang didukung
- ✅ Contoh penggunaan dengan curl/fetch
- ✅ Search fields dan ordering options

**Example dari Swagger UI:**
```
GET /api/warga/
Deskripsi: API endpoint untuk mengelola data warga kelurahan
Parameters:
  - search (query, optional): Cari warga berdasarkan nama_lengkap, NIK, atau alamat
  - ordering (query, optional): Urutkan berdasarkan nama_lengkap atau tanggal_registrasi
  - page (query, optional): Nomor halaman untuk pagination
```

### Token Authentication di Swagger UI

1. **Dapatkan Token:**
   - Method 1: Via Swagger UI → POST `/api/auth/token/`
   - Method 2: Via curl/Postman seperti biasa

2. **Set Authorization:**
   - Klik button "Authorize" 🔓 di Swagger UI
   - Input field: `Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`
   - Klik "Authorize"
   - Icon berubah jadi 🔒 (locked/authenticated)

3. **Test Endpoints:**
   - Sekarang semua requests akan include Authorization header
   - Test protected endpoints seperti POST/PUT/DELETE
   - Test `/api/pengaduan/` yang require authentication

### Konfigurasi Dokumentasi

File: `data_kelurahan/settings.py`

```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'API Aplikasi Warga Kelurahan',
    'DESCRIPTION': 'Dokumentasi API untuk mengelola data warga dan pengaduan...',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SECURITY': [{'tokenAuth': []}],
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
    },
}
```

### Keuntungan drf-spectacular
- ✅ **Automatic**: Generate dari kode existing, tidak perlu manual
- ✅ **Accurate**: Selalu sync dengan implementasi actual
- ✅ **Interactive**: Testing langsung dari dokumentasi
- ✅ **Professional**: Standar industri (OpenAPI 3.0)
- ✅ **Team Collaboration**: Frontend dev bisa mulai bekerja sebelum backend selesai
- ✅ **Onboarding**: Developer baru bisa langsung productive

## Test Files

### 1. Insomnia Collection
**File**: `Insomnia_P9_P10_API_Tests.yaml`
- 24+ pre-configured API requests
- Organized in 7 folders by feature
- Environment variables for easy configuration
- Complete coverage of P9 & P10 features

### 2. Python Test Script
**File**: `test_api_features.py`
- Automated testing script
- 8 comprehensive test functions
- Interactive token authentication
- Run with: `python test_api_features.py`

### 3. Implementation Summary
**File**: `IMPLEMENTATION_SUMMARY.md`
- Complete implementation documentation
- Files modified/created list
- Testing results
- API endpoints summary

## Referensi

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [DRF Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [DRF Filtering](https://www.django-rest-framework.org/api-guide/filtering/)
- [DRF Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
- [Django CORS Headers](https://github.com/adamchainz/django-cors-headers)
- [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Insomnia REST Client](https://insomnia.rest/)
