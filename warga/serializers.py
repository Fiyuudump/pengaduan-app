# warga/serializers.py
from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Tentukan field dari model Warga yang ingin kita ekspos di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)

    class Meta:
        model = Pengaduan
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor', 'pelapor_nama']
