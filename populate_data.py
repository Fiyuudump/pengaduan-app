import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_kelurahan.settings')
django.setup()

from warga.models import Warga, Pengaduan

# Create some sample Warga data
warga1, created = Warga.objects.get_or_create(
    nik='3501234567890001',
    defaults={
        'nama_lengkap': 'Ahmad Santoso',
        'alamat': 'Jl. Merdeka No. 123, RT 01/RW 02',
        'no_telepon': '081234567890'
    }
)

warga2, created = Warga.objects.get_or_create(
    nik='3501234567890002',
    defaults={
        'nama_lengkap': 'Siti Nurhaliza',
        'alamat': 'Jl. Proklamasi No. 45, RT 03/RW 04',
        'no_telepon': '081987654321'
    }
)

warga3, created = Warga.objects.get_or_create(
    nik='3501234567890003',
    defaults={
        'nama_lengkap': 'Budi Raharjo',
        'alamat': 'Jl. Pancasila No. 78, RT 02/RW 01',
        'no_telepon': '081555666777'
    }
)

# Create some sample Pengaduan data
pengaduan1, created = Pengaduan.objects.get_or_create(
    judul='Jalan Berlubang di RT 01',
    defaults={
        'deskripsi': 'Jalan di depan rumah sudah berlubang besar dan mengganggu kendaraan yang lewat.',
        'pelapor': warga1,
        'status': 'BARU'
    }
)

pengaduan2, created = Pengaduan.objects.get_or_create(
    judul='Lampu Jalan Mati',
    defaults={
        'deskripsi': 'Lampu jalan di Jl. Proklamasi sudah mati sejak seminggu lalu.',
        'pelapor': warga2,
        'status': 'DIPROSES'
    }
)

pengaduan3, created = Pengaduan.objects.get_or_create(
    judul='Saluran Air Tersumbat',
    defaults={
        'deskripsi': 'Saluran air di RT 01 tersumbat menyebabkan banjir saat hujan.',
        'pelapor': warga1,
        'status': 'SELESAI'
    }
)

print("Data populated successfully!")
print(f"Total Warga: {Warga.objects.count()}")
print(f"Total Pengaduan: {Pengaduan.objects.count()}")
