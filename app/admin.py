from django.contrib import admin
from django import forms
from app.models import Pembayaran, Kelas, Spp, MetodePembayaran

# Register your models here.
admin.site.register(Spp)
admin.site.register(Pembayaran)
admin.site.register(Kelas)
admin.site.register(MetodePembayaran)