from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import LoginForm, SiswaSignUpForm, PetugasSignUpForm, UserProfileForm
from .models import Siswa, User
from app.models import Pembayaran

@user_passes_test(lambda u: u.is_superuser)
def hapus_user(request, id_user):

    user = User.objects.filter(id=id_user)
    user.delete()
    messages.success(request, "User berhasil dihapus!")
        
    return redirect('data-user')
    
@user_passes_test(lambda u: u.is_superuser)
def data_user(request):
    users = User.objects.all().order_by('id')

    if request.GET:
        search_query = request.GET.get('search_box', None)
        staff_filter = request.GET.get('staff_filter', None)
        siswa_filter = request.GET.get('siswa_filter', None)
        if search_query:
            users = User.objects.filter(Q(nama__contains=search_query) | Q(username__contains=search_query)).order_by('id')
            if users.count() < 1:
                messages.error(request, "Data yang dicari tidak ada!")
        elif staff_filter:
            users = User.objects.filter(is_staff=staff_filter)
        elif siswa_filter:
            users = User.objects.filter(is_siswa=siswa_filter)
        
    paginator = Paginator(users, 5) # Show 5 user per page

    page = request.GET.get('page')
    users_paginator = paginator.get_page(page)
    count_petugas = User.objects.filter(is_staff=1).count()
    count_siswa = User.objects.filter(is_siswa=1).count()

    context = {
        'users': users_paginator,
        'count_siswa': count_siswa,
        'count_petugas': count_petugas,
    }
    return render(request, 'administrator/data-user.html', context)

@login_required(login_url="/login/")
def profile(request, id_user):
    UserProfile = User.objects.get(id=id_user)
    template = 'profile.html'
    if request.POST:
        form = UserProfileForm(request.POST, request.FILES, instance=UserProfile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile berhasil diperbaharui!")
            return redirect('/profile/ubah/' + str(id_user))
    else:
        form = UserProfileForm(instance=UserProfile)
        context = {
            'form': form,
            'UserProfile': UserProfile,
        }

    return render(request, template, context)

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("/admin/")
            
        return redirect("home")

    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("/")
            else:    
                msg = 'Username atau Password salah!'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

@user_passes_test(lambda u: u.is_superuser)
def register_siswa(request):
    if request.method == "POST":
        form = SiswaSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun Siswa Berhasil Dibuat")

            return redirect("data-user")
        else:
            msg = 'Form is not valid'    
    else:
        form = SiswaSignUpForm()

    return render(request, "administrator/register-siswa.html", {"form": form })

@user_passes_test(lambda u: u.is_superuser)
def register_petugas(request):
    if request.method == "POST":
        form = PetugasSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun Petugas Berhasil Dibuat")

            return redirect("data-user")
        else:
            msg = 'Form is not valid'    
    else:
        form = PetugasSignUpForm()

    return render(request, "administrator/register-petugas.html", { "form": form })