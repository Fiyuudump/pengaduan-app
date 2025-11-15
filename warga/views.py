# warga/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

class WargaListView(ListView):
    model = Warga
    # Django secara otomatis akan mencari template di:
    # <nama_app>/<nama_model>_list.html -> warga/warga_list.html

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# Impor baru untuk DRF
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import WargaSerializer, PengaduanSerializer

# --- API VIEWS ---
class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola data warga kelurahan.
    
    Fitur:
    - **P9 (Authentication)**: Public dapat membaca, user authenticated dapat menulis
    - **P10 (Search)**: Pencarian berdasarkan nama_lengkap, NIK, atau alamat
    - **P10 (Ordering)**: Pengurutan berdasarkan nama_lengkap atau tanggal_registrasi
    - **P10 (Pagination)**: 10 item per halaman
    
    Query Parameters:
    - `search`: Cari warga (contoh: ?search=Budi)
    - `ordering`: Urutkan data (contoh: ?ordering=nama_lengkap atau ?ordering=-tanggal_registrasi)
    - `page`: Nomor halaman (contoh: ?page=2)
    
    Contoh Penggunaan:
    - GET /api/warga/ - List semua warga (paginated)
    - GET /api/warga/?search=Budi - Cari warga dengan kata kunci "Budi"
    - GET /api/warga/?ordering=nama_lengkap - Urutkan berdasarkan nama A-Z
    - POST /api/warga/ - Tambah warga baru (requires authentication)
    - PUT /api/warga/{id}/ - Update warga (requires authentication)
    - DELETE /api/warga/{id}/ - Hapus warga (requires authentication)
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # P9: Read-only for public

    # P10: Filtering, Searching, and Ordering
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk mengelola data pengaduan warga.
    
    Fitur:
    - **P9 (Authentication)**: Hanya user authenticated yang dapat mengakses
    - **P10 (Search)**: Pencarian berdasarkan judul atau deskripsi pengaduan
    - **P10 (Ordering)**: Pengurutan berdasarkan status atau tanggal_lapor
    - **P10 (Pagination)**: 10 item per halaman
    
    Query Parameters:
    - `search`: Cari pengaduan (contoh: ?search=lampu)
    - `ordering`: Urutkan data (contoh: ?ordering=status atau ?ordering=-tanggal_lapor)
    - `page`: Nomor halaman (contoh: ?page=2)
    
    Contoh Penggunaan:
    - GET /api/pengaduan/ - List semua pengaduan (requires authentication)
    - GET /api/pengaduan/?search=jalan - Cari pengaduan terkait "jalan"
    - GET /api/pengaduan/?ordering=-tanggal_lapor - Urutkan terbaru ke terlama
    - POST /api/pengaduan/ - Tambah pengaduan baru (requires authentication)
    - PUT /api/pengaduan/{id}/ - Update pengaduan (requires authentication)
    - DELETE /api/pengaduan/{id}/ - Hapus pengaduan (requires authentication)
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticated]  # P9: Authenticated users only

    # P10: Filtering, Searching, and Ordering
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']

