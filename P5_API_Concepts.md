# Framework Programming - Pertemuan 5: API Concepts & JSON

## Konsep Fundamental yang Dipelajari

### 1. Arsitektur Monolitik vs Decoupled
- **Monolitik**: Backend dan Frontend dalam satu proyek (seperti aplikasi Django kita saat ini)
- **Decoupled**: Backend (API) dan Frontend terpisah sepenuhnya

### 2. API (Application Programming Interface)
- **Analogi Restoran**: API adalah pelayan yang menjembatani antara Anda (Frontend/Klien) dan Dapur (Backend/Server)
- Mendefinisikan "menu" (operasi yang tersedia) dan "aturan" (cara berkomunikasi)

### 3. REST (Representational State Transfer)
- **Berbasis Sumber Daya**: Setiap data adalah "resource" dengan alamat unik (URL/URI)
- **HTTP Methods**: 
  - GET: Membaca data (Read)
  - POST: Membuat data baru (Create)
  - PUT/PATCH: Memperbarui data (Update)
  - DELETE: Menghapus data (Delete)
- **Stateless**: Setiap request berisi semua informasi yang dibutuhkan

### 4. JSON (JavaScript Object Notation)
- Format teks ringan untuk pertukaran data
- **Objek {}**: Pasangan kunci:nilai
- **Array []**: Daftar nilai

Contoh JSON untuk Data Warga:
```json
{
  "nik": "3501234567890001",
  "nama_lengkap": "Budi Santoso",
  "alamat": "Jl. Merdeka No. 10",
  "no_telepon": "081234567890"
}
```

## Praktikum dengan API Publik (reqres.in)

### Endpoint yang Diuji:
1. **GET** `https://reqres.in/api/users?page=2` - Daftar pengguna
2. **GET** `https://reqres.in/api/users/2` - Detail pengguna
3. **POST** `https://reqres.in/api/users` - Membuat pengguna baru
4. **GET** `https://reqres.in/api/users/99` - Test 404 Not Found

### Tools yang Digunakan:
- Postman atau Insomnia untuk testing API
- Browser untuk melihat response

### Status Codes yang Dipelajari:
- **200 OK**: Request berhasil
- **201 Created**: Data berhasil dibuat
- **404 Not Found**: Resource tidak ditemukan

## Persiapan untuk Pertemuan Selanjutnya
Dengan pemahaman konsep API ini, kita siap untuk mengimplementasikan Django REST Framework di pertemuan berikutnya.
