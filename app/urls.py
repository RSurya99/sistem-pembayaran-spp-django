# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import tambah_pembayaran, riwayat_pembayaran, hapus_pembayaran, ubah_pembayaran, list_pembayaran, export_xls, data_pembayaran, hapus_spp, ubah_spp, hapus_mp, ubah_mp, tambah_spp, tambah_mp, data_kelas, hapus_kelas, ubah_kelas, tambah_kelas

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('tambah-pembayaran/', tambah_pembayaran, name='tambah-pembayaran'),
    path('riwayat-pembayaran/', riwayat_pembayaran, name='riwayat-pembayaran'),
    path('list-pembayaran/', list_pembayaran, name='list-pembayaran'),
    path('pembayaran/hapus/<int:id_pembayaran>', hapus_pembayaran, name='hapus-pembayaran'),
    path('pembayaran/ubah/<int:id_pembayaran>', ubah_pembayaran, name='ubah-pembayaran'),
    path('export/xls/', export_xls, name='export-xls'),
    path('data-pembayaran/', data_pembayaran, name='data-pembayaran'),
    path('data-pembayaran/hapus/spp/<int:id_spp>', hapus_spp, name='hapus-spp'),
    path('data-pembayaran/ubah/spp/<int:id_spp>', ubah_spp, name='ubah-spp'),
    path('data-pembayaran/hapus/metode-pembayaran/<int:id_mp>', hapus_mp, name='hapus-mp'),
    path('data-pembayaran/ubah/metode-pembayaran/<int:id_mp>', ubah_mp, name='ubah-mp'),
    path('tambah-spp/', tambah_spp, name='tambah-spp'),
    path('tambah-mp/', tambah_mp, name='tambah-mp'),
    path('data-kelas/', data_kelas, name='data-kelas'),
    path('data-kelas/hapus/<int:id_kelas>', hapus_kelas, name='hapus-kelas'),
    path('data-kelas/ubah/<int:id_kelas>', ubah_kelas, name='ubah-kelas'),
    path('tambah-kelas/', tambah_kelas, name='tambah-kelas'),
    
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
