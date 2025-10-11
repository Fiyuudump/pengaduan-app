### Framework Programming **- Pertemuan 3**

**Interaksi Pengguna dengan Django Forms & CreateView**

Alokasi Waktu: 1 Sesi (Estimasi: 3 SKS / 150 menit)

#### **1. Tujuan Pembelajaran (Learning Objectives)**

Setelah menyelesaikan sesi ini, mahasiswa diharapkan mampu:

* Menjelaskan peran Django Forms dalam menangani input, validasi, dan keamanan data dari pengguna.
* Membuat form secara otomatis dari sebuah Model menggunakan ModelForm.
* Mengimplementasikan *generic Class-Based View* CreateView untuk menangani logika pembuatan objek baru.
* Merender form di dalam template dan memahami cara kerja {% csrf\_token %}.
* Mengkonfigurasi success\_url untuk mengarahkan pengguna setelah form berhasil disubmit.

#### **2. Studi Kasus Semester: Aplikasi Warga Kelurahan**

Sejauh ini, aplikasi kita hanya bisa menampilkan data yang kita masukkan secara manual melalui halaman admin. Ini tidak praktis untuk penggunaan sehari-hari. Staf kelurahan tentu membutuhkan antarmuka yang lebih ramah untuk mendaftarkan warga baru.

* **Konsep:** Kita akan beralih dari aplikasi yang *read-only* (hanya bisa dibaca) menjadi aplikasi yang interaktif. Pengguna (dalam hal ini, staf kelurahan) harus bisa menambahkan data baru langsung dari halaman web.
* **Tujuan Hari Ini:** Kita akan membuat sebuah halaman web dengan formulir (*form*) untuk mendaftarkan **Warga** baru. Setelah data diisi dan disimpan, aplikasi akan otomatis mengarahkan kembali ke halaman daftar warga.

#### **3. Materi Ajar (Teori - sekitar 50 menit)**

**A. Gerbang Interaksi: Django Forms**

Setiap kali Anda mengisi formulir online (registrasi, login, kontak), Anda sedang berinteraksi dengan *form*. Di Django, Form adalah sebuah *class* yang melakukan tiga tugas penting:![](data:image/jpeg;base64...)

1. **Rendering:** Menyiapkan dan menampilkan field-field input (seperti text box, text area) dalam format HTML.
2. **Validasi:** Memeriksa data yang dikirim oleh pengguna. Apakah emailnya valid? Apakah nomor NIK sudah diisi? Apakah nomor telepon hanya berisi angka? Ini adalah lapisan pertahanan pertama untuk menjaga data kita tetap bersih dan benar.
3. **Processing:** Jika data valid, form akan membersihkan dan mengubahnya menjadi tipe data Python yang sesuai (misalnya, string, integer) sehingga siap untuk disimpan ke database.

**B. ModelForm: Jalan Pintas yang Cerdas**

Membuat form dari nol bisa jadi pekerjaan yang berulang. Jika kita sudah punya **Model**, mengapa kita harus mendefinisikan ulang semua field-nya di dalam form? Di sinilah ModelForm berperan.

ModelForm adalah *helper class* yang memungkinkan kita membuat Form secara otomatis dari sebuah Django Model.

# forms.py
from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
 class Meta:
 model = Warga
 fields = ['nik', 'nama\_lengkap', 'alamat', 'no\_telepon']

Dengan beberapa baris kode ini, Django akan:

* Melihat Warga model.
* Membuat field form yang sesuai untuk nik, nama\_lengkap, alamat, dan no\_telepon.
* Menerapkan aturan validasi dasar yang sudah ada di model (misalnya, max\_length).

**C. CreateView: Sang Eksekutor Form**

Sekarang kita punya Form. Siapa yang akan menampilkannya dan memproses datanya? Jawabannya adalah CreateView.

CreateView adalah *generic Class-Based View* yang dirancang khusus untuk menangani pembuatan objek baru. Ia melakukan semua pekerjaan berat untuk kita:

* Saat diakses dengan metode GET: Ia akan membuat instance form kosong dan menampilkannya di template.
* Saat form disubmit dengan metode POST: Ia akan mengambil data yang dikirim, mengikatnya ke form, menjalankan validasi, dan jika valid, menyimpan data tersebut sebagai objek baru di database.

**D. success\_url: Tujuan Berikutnya**

Setelah pengguna berhasil menyimpan data, apa yang harus terjadi? Tentu kita tidak ingin mereka tetap berada di halaman form. success\_url adalah atribut di CreateView yang memberitahu Django ke mana harus mengarahkan (redirect) pengguna setelah operasi berhasil.

Untuk menghindari *hardcoding* URL, kita akan menggunakan fungsi reverse\_lazy. Fungsi ini akan mencari URL berdasarkan **nama** yang kita definisikan di urls.py, membuatnya lebih fleksibel jika suatu saat kita mengubah struktur URL.

#### **4. Sesi Praktikum (Sekitar 70 menit)**

**Tujuan: Membuat Halaman Pendaftaran Warga Baru**

Langkah 1: Membuat forms.py

Ini adalah konvensi yang baik untuk meletakkan semua definisi form dalam satu file.

1. Buat file baru di dalam direktori aplikasi warga: warga/forms.py.
2. Isi file tersebut dengan kode berikut:
   # warga/forms.py
   from django import forms
   from .models import Warga

   class WargaForm(forms.ModelForm):
    class Meta:
    model = Warga
    # Tentukan field mana saja dari model yang ingin ditampilkan di form
    fields = ['nik', 'nama\_lengkap', 'alamat', 'no\_telepon']

**Langkah 2: Membuat CreateView**

1. Buka warga/views.py.
2. Impor CreateView, WargaForm, dan reverse\_lazy.
3. Tambahkan class view baru di bawah view yang sudah ada.
   # warga/views.py
   from django.urls import reverse\_lazy
   from django.views.generic import ListView, DetailView, CreateView # Tambahkan CreateView
   from .models import Warga, Pengaduan
   from .forms import WargaForm # Impor form yang baru dibuat

   # ... (WargaListView, WargaDetailView, PengaduanListView) ...

   class WargaCreateView(CreateView):
    model = Warga
    form\_class = WargaForm
    template\_name = 'warga/warga\_form.html'
    success\_url = reverse\_lazy('warga-list') # Arahkan ke daftar warga setelah sukses
   * form\_class: Memberitahu CreateView untuk menggunakan WargaForm.
   * template\_name: Django secara default akan mencari template bernama <model\_name>\_form.html. Kita menentukannya secara eksplisit di sini.

**Langkah 3: Membuat Template Form**

1. Buat file baru: warga/templates/warga/warga\_form.html.
2. Isi dengan kode berikut:
   <!DOCTYPE html>
   <html>
   <head>
    <title>Tambah Warga Baru</title>
   </head>
   <body>
    <h1>Form Pendaftaran Warga Baru</h1>
    <form method="post">
    {% csrf\_token %}
    {{ form.as\_p }}
    <button type="submit">Simpan</button>
    </form>
   </body>
   </html>
   * method="post": Wajib untuk mengirim data.
   * {% csrf\_token %}: **Sangat Penting!** Ini adalah token keamanan Django untuk mencegah serangan *Cross-Site Request Forgery*. Tanpa ini, form tidak akan berfungsi.
   * {{ form.as\_p }}: Perintah ajaib yang akan merender semua field form kita, masing-masing dibungkus dalam tag paragraf <p>.

**Langkah 4: Menambahkan URL**

1. Buka warga/urls.py dan tambahkan path untuk view baru kita.
   # warga/urls.py
   from django.urls import path
   from .views import WargaListView, WargaDetailView, PengaduanListView, WargaCreateView # Impor view baru

   urlpatterns = [
    path('', WargaListView.as\_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as\_view(), name='warga-tambah'), # URL untuk form tambah
    path('<int:pk>/', WargaDetailView.as\_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as\_view(), name='pengaduan-list'),
   ]

Langkah 5: Menambahkan Link ke Halaman Form

Agar mudah diakses, tambahkan link dari halaman daftar warga ke halaman form.

1. Buka warga/templates/warga/warga\_list.html.
2. Tambahkan link di bagian atas:
   <h1>Daftar Warga</h1>
   <a href="{% url 'warga-tambah' %}">Tambah Warga Baru</a>
   <hr>
   <!-- ... (kode ul untuk daftar warga) ... -->

**Langkah 6: Verifikasi**

1. Jalankan server dan buka halaman daftar warga (/warga/).
2. Klik link "Tambah Warga Baru". Anda akan diarahkan ke halaman form.
3. Coba isi data dan klik "Simpan". Jika berhasil, Anda akan kembali ke halaman daftar dan melihat data baru yang Anda masukkan.

#### **5. Tugas Praktik di Kelas (Challenge - sekitar 30 menit)**

**Judul:** Membuat Form Pengaduan Baru

Instruksi:

Anda sudah bisa menambahkan warga baru. Sekarang, terapkan konsep yang sama untuk membuat halaman di mana pengguna bisa menambahkan Pengaduan baru.

**Petunjuk:**

1. **Form:** Buat PengaduanForm di warga/forms.py menggunakan ModelForm.
2. **View:** Buat PengaduanCreateView di warga/views.py.
3. **Template:** Buat template warga/pengaduan\_form.html.
4. **URL:** Tambahkan path baru di warga/urls.py (misal: pengaduan/tambah/).
5. **Tantangan Utama:** Pengaduan memiliki ForeignKey ke Warga. Form yang dibuat secara otomatis akan menampilkan *dropdown* untuk memilih pelapor. Pastikan ini berfungsi.

#### **6. Penutup & Preview Pertemuan Berikutnya (5 menit)**

* **Rangkuman:** Hari ini adalah lompatan besar bagi aplikasi kita. Kita telah beralih dari aplikasi pasif menjadi aplikasi interaktif dengan mempelajari cara menangani input pengguna menggunakan Django Forms dan CreateView.
* **Preview:** Menambahkan data sudah bisa. Bagaimana dengan mengubah data yang salah atau menghapus data yang sudah tidak relevan? Di pertemuan berikutnya, kita akan melengkapi siklus CRUD (Create, Read, Update, Delete) dengan mempelajari **UpdateView** dan **DeleteView**.