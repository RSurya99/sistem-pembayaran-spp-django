# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from authentication.models import Siswa, Petugas, User
from app.models import Kelas, Spp

class UserProfileForm(forms.ModelForm):
    profile_img = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={              
                "class": "form-control"
            }
        )
    )
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={              
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={              
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'nama', 'profile_img', 'email',)

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SiswaSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
        }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password Verifikasi",                
                "class": "form-control"
        }))
    nama = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
            "placeholder" : "Nama Lengkap",                
            "class": "form-control"
        }))
    nis = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
            "placeholder" : "Nomor Induk Siswa",                
            "class": "form-control"
        }))
    no_telp = forms.CharField(
        required=True,
        widget=forms.NumberInput(
            attrs={
            "placeholder" : "No Telepon",                
            "class": "form-control"
        }))
    kelas = forms.ModelChoiceField(
        queryset=Kelas.objects.all(),
        widget=forms.Select(
            attrs={               
            "class": "form-control"
        }), 
        initial='')
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            "placeholder" : "Email Address",         
            "class": "form-control"
        }))

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_siswa = True
        user.nama = self.cleaned_data.get('nama')
        user.email = self.cleaned_data.get('email')
        user.save()
        siswa = Siswa.objects.create(user=user)
        siswa.nis = self.cleaned_data.get('nis')
        siswa.id_kelas = self.cleaned_data.get('kelas')
        siswa.no_telp = self.cleaned_data.get('no_telp')
        siswa.save()
        return user

class PetugasSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
        }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
        }))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password Verifikasi",                
                "class": "form-control"
        }))
    nama = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
            "placeholder" : "Nama Lengkap Petugas",                
            "class": "form-control"
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={        
            "placeholder" : "Email Address",      
            "class": "form-control"
        }))

    class Meta(UserCreationForm.Meta):
        model = User
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_petugas = True
        user.is_staff = True
        user.nama = self.cleaned_data.get('nama')
        user.email = self.cleaned_data.get('email')
        user.save()
        petugas = Petugas.objects.create(user=user)
        petugas.save()
        return user