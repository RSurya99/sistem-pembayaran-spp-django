from django.db import models
from django.contrib.auth.models import AbstractUser
from app.models import Spp, Kelas

class User(AbstractUser):
    is_petugas = models.BooleanField(default=False)
    is_siswa = models.BooleanField(default=False)
    nama = models.CharField(max_length=225, null=True)
    profile_img = models.ImageField(upload_to='profile/', null=True, default='profile-picture-default.jpg')
    email = models.EmailField(null=True)

class Siswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nis = models.CharField(max_length=12, unique=True)
    id_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)
    no_telp = models.CharField(max_length=14)

    def __str__(self):
        return str(self.user) + ' Kelas = ' + str(self.id_kelas)

class Petugas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user.nama)