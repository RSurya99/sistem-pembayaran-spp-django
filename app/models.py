from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spp(models.Model):
    tahun = models.IntegerField()
    nominal = models.IntegerField()

    def __str__(self):
        return str(self.tahun) + ' - Rp' + str(f"{self.nominal:,}")

class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=10)
    kompetensi_keahlian = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kelas + ' ' + self.kompetensi_keahlian

class MetodePembayaran(models.Model):
    metode = models.CharField(max_length=50, null=True)
    keterangan = models.CharField(max_length=225, null=True)

    def __str__(self):
        return self.metode + ' Ke ' + self.keterangan

class Pembayaran(models.Model):
    # id_petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE, null=True)
    # id_siswa = models.ForeignKey("authentication.User", on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = (
        ('pending', 'Pending'), 
        ('success', 'Success'),
        ('rejected', 'Rejected'),
    )

    siswa = models.CharField(max_length=225, null=True)
    tgl_bayar = models.DateField(auto_now_add=True, null=True)
    waktu_dibayar = models.TimeField(auto_now_add=True, null=True)
    id_spp = models.ForeignKey(Spp, on_delete=models.CASCADE, null=True)
    jumlah_bayar = models.IntegerField()
    metode_pembayaran = models.ForeignKey(MetodePembayaran, on_delete=models.CASCADE, null=True)
    status_pembayaran = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    bukti_pembayaran = models.ImageField(upload_to='bukti-pembayaran/', null=True)
    keterangan = models.TextField(null=True)
    nama_petugas = models.CharField(max_length=225, null=True)

    def __str__(self):
        return self.siswa + ' spp tahun ' + str(self.id_spp) + ' jumlah bayar = ' + str(self.jumlah_bayar) + 'x'