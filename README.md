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

- `/warga/` - Daftar semua warga (WargaListView)
- `/warga/<id>/` - Detail warga beserta daftar pengaduannya (WargaDetailView)  
- `/warga/pengaduan/` - Daftar semua pengaduan (PengaduanListView)
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

### Admin Interface
- Model registration untuk kemudahan pengelolaan data
- Interface bawaan Django untuk CRUD operations

## Status Implementasi

- ✅ **P1 (Framework Programming - Pertemuan 1)**: Completed
- ✅ **P2 (Framework Programming - Pertemuan 2)**: Completed
- ⏳ **P3**: Belum diimplementasi
- ⏳ **P4**: Belum diimplementasi
- ⏳ **P5**: Belum diimplementasi  
- ⏳ **P6**: Belum diimplementasi

## Teknologi

- **Framework**: Django 5.2.7
- **Database**: SQLite3
- **Python**: 3.13.7
- **Template Engine**: Django Templates
- **Environment**: Virtual Environment (myenv)
