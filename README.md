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

## Struktur Proyek

```
data_kelurahan/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── populate_data.py
├── data_kelurahan/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── warga/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
        └── warga/
            ├── warga_list.html
            ├── warga_detail.html
            └── pengaduan_list.html
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

5. **Membuat Superuser (Opsional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Menjalankan Server:**
   ```bash
   python manage.py runserver
   ```

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
- ListAPIView dan RetrieveAPIView untuk read-only endpoints
- Browsable API untuk testing dan debugging
- Separation of API URLs dari web URLs
- HTTP status codes dan RESTful principles

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

## Teknologi

- **Framework**: Django 5.2.7
- **API Framework**: Django REST Framework
- **Database**: SQLite3
- **Python**: 3.13.7
- **Template Engine**: Django Templates
- **API Format**: JSON
- **Environment**: Virtual Environment (myenv)
