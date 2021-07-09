from django.contrib import admin
from authentication.models import Siswa, Petugas, User

# Register your models here.
admin.site.register(User)
admin.site.register(Siswa)
admin.site.register(Petugas)