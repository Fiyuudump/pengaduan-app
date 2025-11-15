# Framework Programming - P11 Specification

## Topic: Momen "Aha!": Konsumsi API dengan Frontend JavaScript

### Overview
Mata Kuliah: Framework Programming  
Topik: Momen "Aha!": Konsumsi API dengan Frontend JavaScript  
Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:
- Menjelaskan alur interaksi klien-server dalam arsitektur decoupled
- Menjelaskan masalah **CORS (Cross-Origin Resource Sharing)** dan cara mengatasinya di Django
- Menggunakan **JavaScript fetch API** untuk membuat permintaan GET ke endpoint API
- Mem-parsing respons JSON dan secara dinamis me-render data ke dalam halaman HTML
- Memahami bagaimana backend (Django) dan frontend (HTML/JS) dapat dikembangkan dan dijalankan secara terpisah

### Studi Kasus
Kita telah menghabiskan 10 pertemuan untuk membangun sebuah "mesin" backend yang sangat kuat, aman, dan efisien. Mesin ini bisa menyimpan, mengelola, dan menyajikan data warga dalam format JSON. Namun, sejauh ini, hanya kita (developer) yang bisa melihat hasilnya melalui Browsable API atau Postman.

Hari ini, kita akan membangun sisi lainnya: sebuah **klien**. Kita akan membuat halaman web yang sepenuhnya terpisah dari proyek Django kita. Halaman web ini akan bertindak sebagai "pengguna" dari API kita, meminta data, dan menampilkannya dengan cara yang ramah bagi pengguna akhir.

---

## Section 4: Sesi Praktikum (Sekitar 70 menit)

**Tujuan: Menampilkan Daftar Warga di Halaman Web Terpisah**

### Langkah 1: Mengatasi Masalah CORS di Backend Django

#### Mengapa CORS Diperlukan?
Browser memiliki kebijakan keamanan fundamental yang disebut **Same-Origin Policy**. Kebijakan ini mencegah sebuah halaman web (http://situs-A.com) untuk membuat permintaan ke domain yang berbeda (http://api.situs-B.com).

Dalam arsitektur decoupled, frontend dan backend kita **memang** berada di "asal" (origin) yang berbeda. Frontend kita mungkin berjalan di localhost:3000, sementara backend Django kita berjalan di localhost:8000.

**CORS (Cross-Origin Resource Sharing)** adalah mekanisme yang memungkinkan server (backend kita) untuk memberitahu browser bahwa ia mengizinkan permintaan dari origin lain yang spesifik.

#### Implementasi CORS

1. **Hentikan server Django**

2. **Install library django-cors-headers:**
```bash
pip install django-cors-headers
```

3. **Buka `data_kelurahan/settings.py`**  
   Tambahkan `corsheaders` ke `INSTALLED_APPS`:
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
    'corsheaders',  # Tambahkan ini
]
```

4. **Tambahkan CorsMiddleware ke MIDDLEWARE**  
   Posisi di paling atas atau setelah SecurityMiddleware:
```python
# data_kelurahan/settings.py
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Tambahkan ini
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

5. **Konfigurasi CORS di bagian bawah settings.py:**
```python
# data_kelurahan/settings.py
# Izinkan semua origin untuk mengakses API kita (HANYA UNTUK DEVELOPMENT)
CORS_ALLOW_ALL_ORIGINS = True
```

**⚠️ PENTING untuk Production:**
Untuk production, gunakan whitelist spesifik:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-production-domain.com",
]
```

### Langkah 2: Membuat Halaman Frontend

#### Struktur Folder Terpisah
**PENTING:** Buat folder baru **di luar** direktori proyek `data_kelurahan`. Ini untuk menekankan bahwa keduanya adalah proyek terpisah.

1. **Buat folder baru:**
```bash
mkdir view_kelurahan
cd view_kelurahan
```

2. **Buat file `index.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Warga Kelurahan</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        #warga-list-container {
            margin-top: 20px;
        }
        .warga-item {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .warga-item h3 {
            margin: 0 0 10px 0;
            color: #2c3e50;
        }
        .warga-item p {
            margin: 5px 0;
            color: #555;
        }
        .loading {
            text-align: center;
            color: #666;
            font-style: italic;
        }
        .error {
            text-align: center;
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Daftar Warga Kelurahan</h1>
    <div id="warga-list-container">
        <p class="loading">Memuat data...</p>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

### Langkah 3: Menulis Kode JavaScript untuk Mengambil & Menampilkan Data

#### Konsep fetch API
fetch adalah fungsi bawaan browser modern yang memungkinkan kita membuat permintaan jaringan (HTTP requests) dengan sangat mudah.

**Cara Kerja (Promise-based):**
- fetch tidak langsung mengembalikan data
- Ia mengembalikan sebuah "janji" (Promise) bahwa ia akan menyelesaikan permintaan
- Kita menggunakan `.then()` untuk menentukan apa yang harus dilakukan setelah janji itu terpenuhi

**Alur Dasar GET Request:**
```javascript
fetch('http://api.url/endpoint')  // 1. Buat permintaan
  .then(response => response.json())  // 2. Ubah respons menjadi JSON
  .then(data => {  // 3. Lakukan sesuatu dengan data
    console.log(data);
    // Render data ke HTML di sini
  })
  .catch(error => {  // 4. Tangani jika ada error
    console.error('Error:', error);
  });
```

#### Implementasi app.js

1. **Jalankan kembali server Django:**
```bash
python manage.py runserver
```

2. **Buat file `app.js` di folder `view_kelurahan`:**
```javascript
// app.js
document.addEventListener('DOMContentLoaded', () => {
    const wargaListContainer = document.getElementById('warga-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/warga/';

    /**
     * Fungsi untuk membuat elemen HTML untuk setiap warga
     */
    function renderWarga(warga) {
        // Membuat elemen div untuk container warga
        const wargaDiv = document.createElement('div');
        wargaDiv.className = 'warga-item';

        // Membuat elemen nama
        const nama = document.createElement('h3');
        nama.textContent = warga.nama_lengkap;

        // Membuat elemen NIK
        const nik = document.createElement('p');
        nik.textContent = `NIK: ${warga.nik}`;

        // Membuat elemen alamat
        const alamat = document.createElement('p');
        alamat.textContent = `Alamat: ${warga.alamat}`;

        // Membuat elemen telepon (optional)
        if (warga.no_telepon) {
            const telepon = document.createElement('p');
            telepon.textContent = `Telepon: ${warga.no_telepon}`;
            wargaDiv.appendChild(telepon);
        }

        // Memasukkan semua elemen ke dalam container
        wargaDiv.appendChild(nama);
        wargaDiv.appendChild(nik);
        wargaDiv.appendChild(alamat);

        return wargaDiv;
    }

    /**
     * Fungsi utama untuk mengambil data dari API
     */
    function fetchWargaData() {
        fetch(apiUrl)
            .then(response => {
                // Cek apakah response berhasil
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Hapus pesan "Memuat data..."
                wargaListContainer.innerHTML = '';

                // Cek apakah ada data
                if (data.results && data.results.length > 0) {
                    // Render setiap warga
                    data.results.forEach(warga => {
                        const wargaElement = renderWarga(warga);
                        wargaListContainer.appendChild(wargaElement);
                    });
                } else {
                    wargaListContainer.innerHTML = '<p class="error">Tidak ada data warga.</p>';
                }
            })
            .catch(error => {
                // Tangani error
                wargaListContainer.innerHTML = 
                    '<p class="error">Gagal memuat data. Pastikan server backend berjalan.</p>';
                console.error('There has been a problem with your fetch operation:', error);
            });
    }

    // Panggil fungsi untuk fetch data
    fetchWargaData();
});
```

### Langkah 4: Verifikasi

1. **Pastikan server Django berjalan:**
```bash
python manage.py runserver
```

2. **Buka file `index.html` langsung di browser:**
   - Klik kanan pada file → Open with → Chrome/Firefox
   - Atau drag & drop file ke browser

3. **Hasil yang Diharapkan:**
   - Halaman akan menampilkan "Memuat data..." sejenak
   - Kemudian daftar warga dari API akan muncul
   - Setiap warga ditampilkan dalam card dengan nama, NIK, dan alamat

4. **Troubleshooting:**
   - Jika tidak ada data: Pastikan database memiliki data warga
   - Jika error CORS: Periksa konfigurasi CORS di settings.py
   - Jika "Gagal memuat data": Periksa console browser (F12) untuk error detail

---

## Section 5: Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

### Judul: Menambahkan Form Pendaftaran Warga via JavaScript

Saat ini halaman kita hanya bisa menampilkan data. Tambahkan sebuah form HTML di `index.html` dan gunakan JavaScript untuk mengirim data warga baru ke API melalui permintaan POST.

### Petunjuk:

#### 1. Tambahkan Form HTML di `index.html`

Tambahkan sebelum `<div id="warga-list-container">`:

```html
<div class="form-container">
    <h2>Tambah Warga Baru</h2>
    <form id="warga-form">
        <div class="form-group">
            <label for="nik">NIK:</label>
            <input type="text" id="nik" name="nik" required 
                   pattern="[0-9]{16}" title="NIK harus 16 digit angka">
        </div>
        
        <div class="form-group">
            <label for="nama_lengkap">Nama Lengkap:</label>
            <input type="text" id="nama_lengkap" name="nama_lengkap" required>
        </div>
        
        <div class="form-group">
            <label for="alamat">Alamat:</label>
            <textarea id="alamat" name="alamat" required rows="3"></textarea>
        </div>
        
        <div class="form-group">
            <label for="no_telepon">No. Telepon:</label>
            <input type="tel" id="no_telepon" name="no_telepon" 
                   pattern="[0-9]{10,15}" title="Nomor telepon 10-15 digit">
        </div>
        
        <button type="submit">Tambah Warga</button>
    </form>
    <div id="form-message"></div>
</div>
```

#### 2. Tambahkan CSS untuk Form

Tambahkan di bagian `<style>`:

```css
.form-container {
    background: white;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-container h2 {
    margin-top: 0;
    color: #2c3e50;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    color: #555;
    font-weight: bold;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #3498db;
}

button[type="submit"] {
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
}

button[type="submit"]:hover {
    background-color: #2980b9;
}

#form-message {
    margin-top: 15px;
    padding: 10px;
    border-radius: 4px;
    display: none;
}

#form-message.success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    display: block;
}

#form-message.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    display: block;
}
```

#### 3. Tambahkan JavaScript untuk Handle Form Submit

Tambahkan di `app.js` sebelum pemanggilan `fetchWargaData()`:

```javascript
/**
 * Fungsi untuk menampilkan pesan
 */
function showMessage(message, type) {
    const messageDiv = document.getElementById('form-message');
    messageDiv.textContent = message;
    messageDiv.className = type;
    
    // Auto hide setelah 5 detik
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 5000);
}

/**
 * Fungsi untuk submit form warga baru
 */
function handleFormSubmit(event) {
    event.preventDefault();  // Mencegah halaman reload
    
    // Ambil data dari form
    const formData = {
        nik: document.getElementById('nik').value,
        nama_lengkap: document.getElementById('nama_lengkap').value,
        alamat: document.getElementById('alamat').value,
        no_telepon: document.getElementById('no_telepon').value || ''
    };
    
    // Kirim data ke API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Jika API memerlukan authentication, tambahkan token:
            // 'Authorization': 'Token YOUR_TOKEN_HERE'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Gagal menambahkan warga');
        }
        return response.json();
    })
    .then(data => {
        // Tampilkan pesan sukses
        showMessage('Warga berhasil ditambahkan!', 'success');
        
        // Reset form
        document.getElementById('warga-form').reset();
        
        // Refresh daftar warga
        fetchWargaData();
    })
    .catch(error => {
        // Tampilkan pesan error
        showMessage('Gagal menambahkan warga: ' + error.message, 'error');
        console.error('Error:', error);
    });
}

// Tambahkan event listener untuk form
const wargaForm = document.getElementById('warga-form');
if (wargaForm) {
    wargaForm.addEventListener('submit', handleFormSubmit);
}
```

### Hasil yang Diharapkan

Setelah implementasi lengkap:
1. ✅ Form input warga muncul di atas daftar warga
2. ✅ User dapat mengisi NIK, nama, alamat, dan telepon
3. ✅ Validasi input bekerja (NIK 16 digit, telepon 10-15 digit)
4. ✅ Saat submit, data dikirim ke API via POST
5. ✅ Jika berhasil: pesan sukses muncul, form reset, daftar warga refresh
6. ✅ Jika gagal: pesan error muncul
7. ✅ Warga baru langsung muncul di daftar tanpa refresh halaman

### Catatan untuk Authentication

Jika API Anda menggunakan `IsAuthenticated` permission (bukan `IsAuthenticatedOrReadOnly`), Anda perlu menambahkan token di header:

```javascript
headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
}
```

Untuk mendapatkan token, bisa menggunakan form login terpisah yang memanggil `/api/auth/token/`.

---

## Penutup & Preview

### Rangkuman
Selamat! Hari ini adalah salah satu momen terpenting dalam perjalanan Anda sebagai developer. Anda telah berhasil menjembatani dunia backend dan frontend, membuktikan bahwa aplikasi Django Anda bisa menjadi sumber data yang kuat untuk berbagai jenis klien.

**Yang telah dipelajari:**
- ✅ Konsep arsitektur decoupled (backend & frontend terpisah)
- ✅ CORS dan cara mengatasinya
- ✅ JavaScript fetch API untuk konsumsi API
- ✅ Manipulasi DOM untuk render data dinamis
- ✅ POST request untuk mengirim data ke server

### Preview Pertemuan Berikutnya
Aplikasi kita sudah berfungsi penuh dari ujung ke ujung. Langkah terakhir sebelum siap "go public" adalah profesionalisme. Di pertemuan selanjutnya, kita akan belajar cara membuat **dokumentasi API** secara otomatis menggunakan tools seperti Swagger/OpenAPI. Dokumentasi yang baik adalah kunci agar developer lain (atau diri kita di masa depan) bisa dengan mudah memahami dan menggunakan API yang telah kita buat.
