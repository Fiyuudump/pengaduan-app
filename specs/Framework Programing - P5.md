### Framework programming- Pertemuan 5

**Konsep Fundamental API & Dunia JSON**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menjelaskan perbedaan antara arsitektur **Monolitik** dan **Decoupled (Headless)**.
* Mendefinisikan apa itu **API (Application Programming Interface)** menggunakan analogi yang mudah dipahami.
* Menjelaskan tujuan **REST (Representational State Transfer)** sebagai gaya arsitektur untuk desain API.
* Memahami struktur dan sintaks dasar **JSON (JavaScript Object Notation)** sebagai format pertukaran data.
* Menggunakan *API client tool* (seperti Postman atau browser) untuk membuat request ke API publik dan menganalisis respons JSON yang diterima.

#### 2. Studi Kasus Semester: Aplikasi Warga Kelurahan

Selama empat pertemuan, kita telah membangun aplikasi web yang fungsional di mana Django bertindak sebagai backend sekaligus frontend (melalui rendering template). Ini disebut arsitektur **Monolitik**.

* **Pergeseran Paradigma:** Bayangkan jika Bapak Lurah ingin membuat aplikasi mobile untuk Android & iOS agar warga bisa melihat pengumuman, atau sebuah dashboard modern di kantornya yang menampilkan data secara *real-time*. Aplikasi Django kita saat ini tidak bisa melayani kebutuhan tersebut karena hanya menghasilkan HTML.
* **Tujuan Hari Ini:** Kita akan jeda sejenak dari *coding* Django untuk memahami "mengapa" kita perlu API. Kita akan belajar bagaimana aplikasi kita bisa berevolusi dari sekadar situs web menjadi sebuah **pusat data** yang bisa melayani berbagai jenis klien (web, mobile, dll).

#### 3. Materi Ajar (Teori - sekitar 60 menit)

**A. Pergeseran Arsitektur: Dari Monolitik ke *Decoupled***

* **Arsitektur Monolitik (Yang Telah Kita Bangun):**
  + Backend (Django) dan Frontend (Template HTML) berada dalam satu proyek yang sama dan saling terikat erat.
  + Django bertanggung jawab atas logika bisnis, interaksi database, **DAN** pembuatan HTML yang dilihat pengguna.
  + **Analogi:** Membeli sebuah komputer *All-in-One*. CPU, monitor, dan speaker sudah menjadi satu paket. Praktis, tapi sulit untuk di-upgrade secara terpisah.
* **Arsitektur Decoupled / Headless (Tujuan Kita):**
  + Backend dan Frontend adalah dua aplikasi yang **terpisah sepenuhnya**.
  + **Tugas Backend (Django):** Hanya satu, yaitu mengelola data dan menyediakannya melalui sebuah **API**. Ia tidak lagi peduli dengan tampilan (HTML, CSS). Ia menjadi "headless" (tanpa kepala/tampilan).
  + **Tugas Frontend (React, Vue, Aplikasi Mobile):** Mengambil data dari API dan menampilkannya kepada pengguna.
  + **Analogi:** Merakit PC sendiri. Anda bisa memilih monitor, CPU, dan speaker terbaik secara terpisah dan menghubungkannya dengan kabel standar (API).

**B. Apa itu API? Sang Pelayan Digital**

**API (Application Programming Interface)** adalah perantara yang memungkinkan dua aplikasi berbeda untuk saling berbicara.

* **Analogi Restoran yang Paling Terkenal:**
  + **Anda (Frontend/Klien):** Ingin memesan makanan.
  + **Dapur (Backend/Server & Database):** Tempat makanan dibuat. Anda tidak bisa langsung masuk ke dapur.
  + **Pelayan (API):** Anda memberikan pesanan (Request) kepada pelayan. Pelayan mencatatnya, meneruskannya ke dapur dengan bahasa yang dimengerti dapur, lalu mengambil makanan yang sudah jadi (Response) dan mengantarkannya ke meja Anda.

API mendefinisikan "menu" (operasi apa yang tersedia) dan "aturan" (bagaimana cara memesan) yang harus diikuti.

**C. REST: Aturan Main Komunikasi**

**REST (Representational State Transfer)** bukanlah sebuah teknologi, melainkan sebuah **gaya arsitektur** atau serangkaian aturan dan prinsip untuk mendesain API agar mudah dipahami dan digunakan.

* **Berbasis Sumber Daya (Resource):** Setiap data dianggap sebagai "sumber daya" yang memiliki alamat unik (URL/URI).
  + /warga/ -> Daftar semua warga.
  + /warga/1/ -> Data warga dengan ID 1.
  + /warga/1/pengaduan/ -> Daftar pengaduan dari warga dengan ID 1.
* **Menggunakan Metode HTTP (Verbs):** Kita memanfaatkan metode standar HTTP untuk melakukan operasi CRUD.
  + GET: Membaca data (Read).
  + POST: Membuat data baru (Create).
  + PUT/PATCH: Memperbarui data (Update).
  + DELETE: Menghapus data (Delete).
* **Stateless (Tanpa Status):** Setiap *request* dari klien harus berisi semua informasi yang dibutuhkan server untuk memprosesnya. Server tidak menyimpan informasi tentang sesi klien di antara *request*.

**D. JSON: Bahasa Universal API**

Jika API adalah pelayan, **JSON (JavaScript Object Notation)** adalah bahasa yang mereka gunakan. Ini adalah format teks ringan untuk pertukaran data yang mudah dibaca oleh manusia dan mudah di-parse oleh mesin.

* **Struktur Dasar:**
  + **Objek {}:** Kumpulan pasangan kunci:nilai (seperti *dictionary* di Python).
  + **Array []:** Daftar nilai (seperti *list* di Python).
* **Contoh JSON untuk Data Warga:**
  {
   "nik": "3501234567890001",
   "nama\_lengkap": "Budi Santoso",
   "alamat": "Jl. Merdeka No. 10",
   "no\_telepon": "081234567890"
  }

#### 4. Sesi Praktikum (Sekitar 60 menit)

**Tujuan: Menjadi Konsumen API untuk Pertama Kalinya**

Hari ini kita tidak akan menulis kode Django. Kita akan berada di sisi lain: menjadi aplikasi klien yang meminta data dari API publik yang sudah ada.

**Alat:** Kita akan menggunakan **Postman** (atau alternatif seperti Insomnia/ReqBin). Postman adalah aplikasi standar industri untuk menguji API.

**API Publik:** Kita akan menggunakan https://reqres.in/, sebuah API gratis untuk pengujian.

**Langkah-langkah:**

1. **Mendapatkan Daftar Pengguna:**
   * Buka Postman.
   * Pilih metode GET.
   * Masukkan URL: https://reqres.in/api/users?page=2
   * Klik "Send".
2. **Analisis Respons:**
   * Lihat **Status Code**: 200 OK (artinya request berhasil).
   * Lihat **Body**: Anda akan melihat data dalam format JSON. Perhatikan strukturnya: sebuah objek yang memiliki kunci data, di mana nilainya adalah sebuah *array* dari objek-objek pengguna.
3. **Mendapatkan Satu Pengguna:**
   * Ubah URL menjadi: https://reqres.in/api/users/2
   * Klik "Send".
4. **Analisis Respons:**
   * Perhatikan Body-nya. Sekarang data utamanya adalah sebuah objek tunggal, bukan array.

#### 5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

**Judul:** Menjadi Detektif API

Instruksi:

Gunakan Postman dan dokumentasi dari https://reqres.in/ untuk menyelesaikan misi berikut:

1. **Misi POST:** Temukan cara untuk **membuat (Create)** pengguna baru.
   * Ubah metode menjadi POST.
   * Gunakan endpoint yang benar (/api/users).
   * Pindah ke tab "Body", pilih "raw" dan "JSON".
   * Kirim data JSON seperti ini: {"name": "Nama Anda", "job": "Mahasiswa"}.
   * Lihat responsnya. Apa status code yang Anda dapatkan? (Seharusnya 201 Created).
2. **Misi 404:** Coba minta data untuk pengguna yang tidak ada.
   * Gunakan metode GET dengan URL https://reqres.in/api/users/99.
   * Apa status code yang Anda dapatkan? (Seharusnya 404 Not Found).

#### 6. Penutup & Preview Pertemuan Berikutnya (5 menit)

* **Rangkuman:** Hari ini kita telah mengambil langkah konseptual yang krusial. Kita sekarang memahami *mengapa* API sangat penting dalam pengembangan aplikasi modern dan bagaimana mereka berkomunikasi menggunakan prinsip REST dan bahasa JSON.
* **Preview:** Dengan bekal pemahaman ini, pertemuan selanjutnya akan sangat menarik. Kita akan mulai menginstal *library* paling populer untuk API di Django: **Django REST Framework (DRF)**. Kita akan membuat *endpoint* API pertama kita yang menyajikan data warga dalam format JSON, bukan lagi HTML.