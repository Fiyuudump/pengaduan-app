### Framework programming- Pertemuan 4

**Melengkapi CRUD dengan UpdateView & DeleteView**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### 1. Tujuan Pembelajaran (Learning Objectives)

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menjelaskan siklus **CRUD (Create, Read, Update, Delete)** secara lengkap dalam konteks aplikasi web.
* Mengimplementasikan *generic Class-Based View* UpdateView untuk mengubah data yang sudah ada.
* Mengimplementasikan *generic Class-Based View* DeleteView untuk menghapus data dengan halaman konfirmasi.
* Memahami cara UpdateView dan DeleteView mengidentifikasi objek spesifik melalui *primary key* (pk) di URL.
* Mengintegrasikan fungsionalitas *Update* dan *Delete* ke dalam alur kerja aplikasi yang sudah ada.

#### 2. Studi Kasus Semester: Aplikasi Warga Kelurahan

Aplikasi kita sudah semakin fungsional. Staf kelurahan kini bisa melihat daftar warga (Read) dan mendaftarkan warga baru (Create). Namun, bagaimana jika terjadi kesalahan saat memasukkan data? Atau jika ada seorang warga yang pindah dan datanya perlu dihapus?

* **Konsep:** Aplikasi yang robust harus menyediakan cara untuk mengelola data secara penuh. Hari ini, kita akan melengkapi dua operasi terakhir dari siklus CRUD: **Update** (memperbarui) dan **Delete** (menghapus).
* **Tujuan Hari Ini:** Kita akan menambahkan tombol "Edit" dan "Hapus" pada halaman detail warga. Tombol "Edit" akan membawa pengguna ke form yang sudah terisi data warga tersebut untuk diubah, dan tombol "Hapus" akan membawa ke halaman konfirmasi sebelum data benar-benar dihilangkan dari sistem.

#### 3. Materi Ajar (Teori - sekitar 45 menit)

**A. UpdateView: Mengubah yang Sudah Ada**

UpdateView sangat mirip dengan CreateView yang sudah kita pelajari. Keduanya menggunakan ModelForm dan sebuah template untuk menampilkan form. Perbedaan utamanya adalah:

1. **Identifikasi Objek:** UpdateView harus tahu **data mana** yang akan diubah. Ia melakukannya dengan mengambil nilai *primary key* (pk) atau slug dari URL.
2. **Pra-pengisian Form (Pre-population):** Saat diakses dengan metode GET, UpdateView akan mengambil objek dari database berdasarkan pk, lalu mengisi form dengan data dari objek tersebut sebelum menampilkannya ke pengguna.

Logikanya sama persis dengan CreateView saat menangani POST: validasi data, dan jika valid, ia akan **memperbarui** objek yang ada, bukan membuat yang baru.

**B. DeleteView: Operasi yang Membutuhkan Konfirmasi**

Menghapus data adalah tindakan destruktif dan tidak dapat diurungkan dengan mudah. Oleh karena itu, praktik terbaik adalah selalu meminta konfirmasi dari pengguna sebelum benar-benar menghapus data. DeleteView dirancang khusus untuk alur kerja ini.

* **Saat diakses dengan GET:** DeleteView akan menampilkan sebuah halaman konfirmasi. Halaman ini biasanya berisi pertanyaan seperti "Apakah Anda yakin ingin menghapus data ini?" dan menampilkan beberapa detail dari data yang akan dihapus.
* **Saat diakses dengan POST:** Halaman konfirmasi akan memiliki sebuah form dengan tombol "Hapus". Ketika tombol ini diklik, ia akan mengirim request POST ke DeleteView, yang kemudian akan menghapus objek dari database dan mengarahkan pengguna ke success\_url.

**C. Pentingnya success\_url dan reverse\_lazy**

Sama seperti CreateView, baik UpdateView maupun DeleteView membutuhkan success\_url untuk memberitahu Django ke mana harus pergi setelah operasi berhasil. Menggunakan reverse\_lazy('nama-url') tetap menjadi praktik terbaik untuk menjaga URL kita tetap fleksibel dan mudah dikelola.

#### 4. Sesi Praktikum (Sekitar 75 menit)

**Tujuan: Menambahkan Fungsionalitas Edit dan Hapus Data Warga**

Langkah 1: Membuat UpdateView untuk Warga

Kita bisa menggunakan kembali WargaForm dan template warga\_form.html yang sudah ada!

1. Buka warga/views.py.
2. Impor UpdateView dan tambahkan class view baru.
   # warga/views.py
   # ... (impor yang sudah ada) ...
   from django.views.generic import ListView, DetailView, CreateView, UpdateView # Tambahkan UpdateView

   # ... (class view yang sudah ada) ...

   class WargaUpdateView(UpdateView):
    model = Warga
    form\_class = WargaForm
    template\_name = 'warga/warga\_form.html' # Kita pakai template yang sama
    success\_url = reverse\_lazy('warga-list')
3. Buka warga/urls.py dan tambahkan path untuk view ini. Perhatikan bahwa URL harus menangkap pk.
   # warga/urls.py
   # ... (impor yang sudah ada) ...
   from .views import WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView # Impor view baru

   urlpatterns = [
    path('', WargaListView.as\_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as\_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as\_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as\_view(), name='warga-edit'), # URL untuk edit
    # ... (URL pengaduan) ...
   ]

**Langkah 2: Membuat DeleteView untuk Warga**

1. Buka warga/views.py.
2. Impor DeleteView dan tambahkan class view baru.
   # warga/views.py
   # ... (impor yang sudah ada) ...
   from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Tambahkan DeleteView

   # ... (class view yang sudah ada) ...

   class WargaDeleteView(DeleteView):
    model = Warga
    template\_name = 'warga/warga\_confirm\_delete.html'
    success\_url = reverse\_lazy('warga-list')
3. Buat template konfirmasi. Buat file baru warga/templates/warga/warga\_confirm\_delete.html:
   <!DOCTYPE html>
   <html>
   <head>
    <title>Konfirmasi Hapus</title>
   </head>
   <body>
    <h1>Hapus Warga</h1>
    <p>Apakah Anda yakin ingin menghapus data warga: <strong>{{ object.nama\_lengkap }}</strong>?</p>
    <form method="post">
    {% csrf\_token %}
    <button type="submit">Ya, Hapus</button>
    <a href="{% url 'warga-detail' object.pk %}">Batal</a>
    </form>
   </body>
   </html>
4. Buka warga/urls.py dan tambahkan path untuk view ini.
   # warga/urls.py
   # ... (impor yang sudah ada) ...
   from .views import WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView, WargaDeleteView # Impor view baru

   urlpatterns = [
    # ... (URL yang sudah ada) ...
    path('<int:pk>/edit/', WargaUpdateView.as\_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as\_view(), name='warga-hapus'), # URL untuk hapus
    # ... (URL pengaduan) ...
   ]

Langkah 3: Menambahkan Link ke Halaman Detail

Sekarang, kita perlu cara untuk mengakses halaman edit dan hapus. Tempat terbaik adalah dari halaman detail warga.

1. Buka warga/templates/warga/warga\_detail.html.
2. Tambahkan link untuk edit dan hapus.
   <!-- warga/templates/warga/warga\_detail.html -->
   <h1>Detail Warga: {{ object.nama\_lengkap }}</h1>

   <a href="{% url 'warga-edit' object.pk %}">Edit Data</a> |
   <a href="{% url 'warga-hapus' object.pk %}">Hapus Data</a>
   <hr>

   <!-- ... (sisa kode untuk menampilkan detail dan daftar pengaduan) ... -->

**Langkah 4: Verifikasi**

1. Jalankan server dan buka halaman daftar warga.
2. Klik salah satu nama warga untuk masuk ke halaman detail.
3. Anda sekarang akan melihat link "Edit Data" dan "Hapus Data".
4. Klik "Edit Data". Anda akan dibawa ke form yang sudah terisi. Coba ubah salah satu data dan simpan.
5. Kembali ke halaman detail, lalu klik "Hapus Data". Anda akan dibawa ke halaman konfirmasi. Klik "Ya, Hapus" untuk menghapus data.

#### 5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)

**Judul:** Melengkapi CRUD untuk Pengaduan

Instruksi:

Anda telah berhasil mengimplementasikan siklus CRUD penuh untuk model Warga. Sekarang, terapkan pola yang sama untuk model Pengaduan.

**Petunjuk:**

1. **View:** Buat PengaduanUpdateView dan PengaduanDeleteView di warga/views.py.
2. **URL:** Tambahkan path URL yang sesuai di warga/urls.py untuk edit dan hapus pengaduan (misal: pengaduan/<int:pk>/edit/).
3. **Template:**
   * Untuk UpdateView, Anda bisa menggunakan kembali template pengaduan\_form.html yang dibuat pada tugas pertemuan sebelumnya.
   * Buat template konfirmasi baru pengaduan\_confirm\_delete.html.
4. **Integrasi:** Tambahkan link "Edit" dan "Hapus" di halaman daftar semua pengaduan (pengaduan\_list.html) atau di halaman detail warga (di samping setiap item pengaduan).

#### 6. Penutup & Preview Pertemuan Berikutnya (5 menit)

* **Rangkuman:** Selamat! Hari ini kita telah berhasil melengkapi siklus CRUD. Aplikasi kita sekarang memiliki fungsionalitas penuh untuk mengelola data: membuat, membaca, memperbarui, dan menghapus. Menguasai pola ListView, DetailView, CreateView, UpdateView, dan DeleteView adalah fondasi yang sangat kuat dalam pengembangan Django.
* **Preview:** Aplikasi kita sudah fungsional, tapi belum "pintar". Di pertemuan selanjutnya, kita akan masuk ke topik yang sangat penting: **Konsep Fundamental API**. Kita akan membahas mengapa aplikasi modern memisahkan backend dan frontend, dan bagaimana Django bisa bertransformasi dari penyaji halaman HTML menjadi penyedia data murni dalam format JSON. Ini adalah langkah pertama kita menuju dunia Django REST Framework.