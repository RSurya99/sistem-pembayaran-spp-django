from django import forms
from app.models import Pembayaran, MetodePembayaran, Spp, Kelas

class FormPembayaran(forms.ModelForm):
    siswa = forms.CharField(
        widget=forms.TextInput(
            attrs={              
                "class": "form-control"
        }))
    nama_petugas = forms.CharField(
        widget=forms.TextInput(
            attrs={              
                "class": "form-control"
        }))
    id_spp = forms.ModelChoiceField(
        queryset=Spp.objects.all(),
        widget=forms.Select(
            attrs={             
            "class": "form-control shadow"
        }))
    jumlah_bayar = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
            "placeholder" : "Masukkan Jumlah Bayar",                
            "class": "form-control shadow"
        }))
    metode_pembayaran = forms.ModelChoiceField(
        queryset=MetodePembayaran.objects.all(),
        widget=forms.Select(
            attrs={               
            "class": "form-control"
        }), 
        initial='')
    bukti_pembayaran = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }))
    keterangan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Masukkan Keterangan",
                "rows": 3,
            }))
    status_pembayaran = forms.ChoiceField(
        choices=Pembayaran.STATUS_CHOICES,
        widget = forms.Select(
            attrs={
                "class": "form-control"
            }))

    class Meta:
        model = Pembayaran
        fields = ('siswa', 'id_spp', 'jumlah_bayar', 'metode_pembayaran', 'bukti_pembayaran', 'keterangan', 'status_pembayaran', 'nama_petugas')
        

class FormPembayaranSiswa(forms.ModelForm):
    siswa = forms.CharField(
        widget=forms.TextInput(
            attrs={              
                "class": "form-control"
        }))
    id_spp = forms.ModelChoiceField(
        queryset=Spp.objects.all(),
        widget=forms.Select(
            attrs={             
            "class": "form-control shadow"
        }))
    jumlah_bayar = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
            "placeholder" : "Masukkan Jumlah Bayar",                
            "class": "form-control shadow"
        }))
    metode_pembayaran = forms.ModelChoiceField(
        queryset=MetodePembayaran.objects.all(),
        widget=forms.Select(
            attrs={               
            "class": "form-control"
        }), 
        initial='')
    bukti_pembayaran = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }))
    keterangan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Masukkan Keterangan",
                "rows": 3,
            }))

    class Meta:
        model = Pembayaran
        fields = ('siswa', 'id_spp', 'jumlah_bayar', 'metode_pembayaran', 'bukti_pembayaran', 'keterangan')

class FormSpp(forms.ModelForm):
    tahun = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={               
            "class": "form-control"
        }))
    nominal = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={               
            "class": "form-control"
        }))

    class Meta:
        model = Spp
        fields = ('tahun', 'nominal')

class FormMetodePembayaran(forms.ModelForm):
    metode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={               
            "class": "form-control"
        }))
    keterangan = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={               
            "class": "form-control"
        }))

    class Meta:
        model = MetodePembayaran
        fields = ('metode', 'keterangan')

class FormKelas(forms.ModelForm):
    nama_kelas = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={               
            "class": "form-control"
        }))
    kompetensi_keahlian = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={               
            "class": "form-control"
        }))

    class Meta:
        model = Kelas
        fields = ('nama_kelas', 'kompetensi_keahlian')