### Framework Programming **- Pertemuan 2**

**Relasi Model & QuerySet Lanjutan**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### **1. Tujuan Pembelajaran (Learning Objectives)**

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menjelaskan konsep relasi database (khususnya *One-to-Many*).
* Mengimplementasikan relasi *One-to-Many* menggunakan ForeignKey di dalam Django Model.
* Memahami cara Django ORM (Object-Relational Mapper) merepresentasikan relasi antar tabel.
* Melakukan *query* untuk mengambil dan menampilkan data yang saling berhubungan di dalam template.
* Menggunakan QuerySet API untuk memfilter data (.filter(), .get()).

#### **2. Studi Kasus Semester: Aplikasi Warga Kelurahan**

Pada pertemuan sebelumnya, kita telah berhasil membuat fondasi aplikasi untuk menampilkan data setiap warga. Sekarang, kita akan menambahkan fungsionalitas baru yang lebih dinamis: **Sistem Pengaduan Warga**.

* **Konsep:** Setiap warga yang terdaftar dapat membuat satu atau lebih catatan pengaduan (misalnya: laporan jalan rusak, lampu jalan mati, dll.). Ini adalah contoh klasik dari relasi **Satu-ke-Banyak** (*One-to-Many*): **Satu** Warga dapat memiliki **Banyak** Pengaduan.
* **Tujuan Hari Ini:** Kita akan membangun model untuk Pengaduan dan menghubungkannya ke model Warga. Kemudian, kita akan menampilkan daftar pengaduan yang dibuat oleh setiap warga di halaman detail mereka.

#### **3. Materi Ajar (Teori - sekitar 50 menit)**

**A. Menghubungkan Data: Relasi Antar Model**

Aplikasi yang baik jarang sekali hanya memiliki satu tabel data yang berdiri sendiri. Data cenderung saling berhubungan. Django ORM menyediakan cara yang elegan untuk mendefinisikan tiga jenis relasi database utama:![](data:image/jpeg;base64...)

1. **Many-to-Many (ManyToManyField):** Hubungan banyak-ke-banyak. Contoh: Satu **Mahasiswa** bisa mengambil banyak **Mata Kuliah**, dan satu **Mata Kuliah** bisa diambil oleh banyak **Mahasiswa**.
2. **One-to-One (OneToOneField):** Hubungan satu-ke-satu. Contoh: Satu **Pengguna** hanya memiliki satu **Profil Pengguna**.
3. **One-to-Many (ForeignKey):** Hubungan satu-ke-banyak. **Fokus kita hari ini.** Ini adalah jenis relasi yang paling umum. Contoh: Satu **Warga** bisa memiliki banyak **Pengaduan**.

**B. ForeignKey: Kunci Penghubung**

ForeignKey adalah sebuah *field* yang kita letakkan pada model di sisi "banyak" untuk menunjuk ke model di sisi "satu".

class Warga(models.Model): # Sisi "Satu"
 # ... fields ...

class Pengaduan(models.Model): # Sisi "Banyak"
 pelapor = models.ForeignKey(Warga, on\_delete=models.CASCADE)
 # ... fields ...

* ForeignKey(Warga, ...): Memberitahu Django bahwa setiap Pengaduan terhubung ke satu Warga.
* on\_delete=models.CASCADE: Ini adalah aturan penting. CASCADE berarti "jika data Warga (sisi 'satu') dihapus, maka semua Pengaduan yang terhubung dengannya juga akan ikut terhapus". Ini menjaga integritas data. Opsi lain termasuk SET\_NULL (mengisi ForeignKey dengan NULL) atau PROTECT (mencegah penghapusan).

**C. QuerySet API: Bertanya pada Database**

QuerySet adalah representasi dari sekumpulan baris data dari database. Django memberikan kita API yang sangat kuat untuk berinteraksi dengannya.

* **Mengambil Semua Objek:** Model.objects.all()
* **Memfilter Objek (.filter()):** Mengembalikan QuerySet baru yang berisi objek yang cocok dengan kriteria. Bisa menghasilkan banyak objek atau tidak sama sekali.
  + Pengaduan.objects.filter(status='Selesai')
* **Mengambil Satu Objek (.get()):** Hanya mengembalikan **satu** objek yang cocok. Akan menghasilkan *error* jika tidak ada objek yang ditemukan atau jika ditemukan lebih dari satu.
  + Warga.objects.get(nik='3501...\_')

**D. Mengakses Data Terkait**

Inilah keajaiban Django ORM. Setelah relasi didefinisikan, kita bisa "melompat" dari satu model ke model lain.

* **Dari "Banyak" ke "Satu":** Sangat mudah. Cukup akses nama field ForeignKey.
  # Diberikan satu objek pengaduan
  pengaduan = Pengaduan.objects.get(pk=1)
  # Kita bisa langsung mendapatkan nama pelapornya
  nama\_pelapor = pengaduan.pelapor.nama\_lengkap
* **Dari "Satu" ke "Banyak":** Django secara otomatis membuat "manager" terbalik. Kita bisa mengakses semua objek terkait dari sisi "banyak" menggunakan sintaks namamodelterkait\_set.
  # Diberikan satu objek warga
  warga = Warga.objects.get(pk=1)
  # Kita bisa mendapatkan semua pengaduan yang pernah dibuat oleh warga ini
  semua\_pengaduan\_warga = warga.pengaduan\_set.all()

#### **4. Sesi Praktikum (Sekitar 70 menit)**

**Tujuan: Mengimplementasikan Sistem Pengaduan Warga**

Langkah 1: Membuat Model Pengaduan

Buka warga/models.py dan tambahkan model baru di bawah model Warga.

# warga/models.py

# ... (Model Warga yang sudah ada) ...

class Pengaduan(models.Model):
 STATUS\_CHOICES = [
 ('BARU', 'Baru'),
 ('DIPROSES', 'Diproses'),
 ('SELESAI', 'Selesai'),
 ]

 judul = models.CharField(max\_length=200)
 deskripsi = models.TextField()
 status = models.CharField(max\_length=10, choices=STATUS\_CHOICES, default='BARU')
 tanggal\_lapor = models.DateTimeField(auto\_now\_add=True)

 # Kunci relasinya ada di sini!
 pelapor = models.ForeignKey(Warga, on\_delete=models.CASCADE, related\_name='pengaduan')

 def \_\_str\_\_(self):
 return self.judul

*Catatan: related\_name='pengaduan' adalah praktik yang baik. Ini memungkinkan kita mengakses dari sisi Warga dengan warga.pengaduan.all() daripada warga.pengaduan\_set.all().*

Langkah 2: Migrasi Database

Karena kita mengubah models.py, kita perlu memperbarui skema database.

1. python manage.py makemigrations
2. python manage.py migrate

**Langkah 3: Mendaftarkan Model ke Admin & Menambah Data**

1. Buka warga/admin.py dan daftarkan model Pengaduan.
   # warga/admin.py
   from django.contrib import admin
   from .models import Warga, Pengaduan # Tambahkan Pengaduan

   admin.site.register(Warga)
   admin.site.register(Pengaduan) # Daftarkan model baru
2. Jalankan server dan buka halaman admin. Sekarang Anda akan melihat menu "Pengaduans".
3. Buat beberapa data pengaduan, dan pastikan untuk memilih pelapor dari data warga yang sudah ada.

Langkah 4: Menampilkan Pengaduan di Halaman Detail Warga

Kita akan memodifikasi template warga\_detail.html untuk menampilkan daftar pengaduan yang relevan.

1. Buka warga/templates/warga/warga\_detail.html.
2. Di bagian bawah, setelah menampilkan detail warga, tambahkan kode berikut:
   <!-- warga/templates/warga/warga\_detail.html -->

   <!-- ... (kode untuk menampilkan detail NIK, alamat, dll) ... -->

   <hr>
   <h2>Daftar Pengaduan oleh {{ object.nama\_lengkap }}</h2>

   <ul>
    {% for aduan in object.pengaduan.all %}
    <li>
    <strong>{{ aduan.judul }}</strong> (Status: {{ aduan.get\_status\_display }})
    <p>{{ aduan.deskripsi }}</p>
    </li>
    {% empty %}
    <li>Warga ini belum pernah membuat pengaduan.</li>
    {% endfor %}
   </ul>
   * object.pengaduan.all: Inilah cara kita mengakses semua pengaduan terkait dari objek Warga yang sedang ditampilkan.
   * aduan.get\_status\_display: Trik Django untuk menampilkan label yang mudah dibaca dari field choices.

**Langkah 5: Verifikasi**

1. Refresh halaman detail salah satu warga di browser.
2. Anda sekarang akan melihat daftar pengaduan yang dibuat oleh warga tersebut.

#### **5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)**

**Judul:** Membuat Halaman Daftar Semua Pengaduan

Instruksi:

Anda telah berhasil menampilkan pengaduan per warga. Sekarang, buatlah sebuah halaman baru yang menampilkan semua pengaduan dari seluruh warga dalam satu daftar.

**Petunjuk:**

1. **View:** Buat sebuah ListView baru bernama PengaduanListView di warga/views.py. Set model = Pengaduan.
2. **Template:** Buat template baru warga/templates/warga/pengaduan\_list.html.
3. **Looping:** Di dalam template, lakukan *looping* pada object\_list.
4. **Tantangan Utama:** Di setiap item daftar, selain menampilkan judul pengaduan, tampilkan juga **nama lengkap warga yang melapor**. (Petunjuk: pengaduan.pelapor.nama\_lengkap).
5. **URL:** Tambahkan path baru di warga/urls.py untuk halaman ini (misal: path('pengaduan/', ...)).

#### **6. Penutup & Preview Pertemuan Berikutnya (5 menit)**

* **Rangkuman:** Hari ini kita telah mempelajari konsep paling fundamental dalam aplikasi berbasis data: relasi. Kita telah berhasil menghubungkan dua model menggunakan ForeignKey dan menampilkan data yang saling terkait, yang membuka jalan untuk membangun aplikasi yang jauh lebih kompleks.
* **Preview:** Sejauh ini kita hanya menampilkan data. Di pertemuan berikutnya, kita akan mulai berinteraksi dengan pengguna. Kita akan belajar cara menggunakan **Django Forms** dan **CreateView** untuk memungkinkan pengguna (misalnya, staf kelurahan) menambahkan data warga baru langsung dari halaman web, bukan lagi dari halaman admin.