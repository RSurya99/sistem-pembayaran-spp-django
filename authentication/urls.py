# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_siswa, register_petugas, profile, data_user, hapus_user
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register-siswa/', register_siswa, name='register-siswa'),
    path('register-petugas/', register_petugas, name='register-petugas'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/ubah/<int:id_user>', profile, name='profile'),
    path('data-user/', data_user, name='data-user'),
    path('data-user/hapus/<int:id_user>', hapus_user, name='hapus-user'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)