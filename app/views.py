from django import template
from django.template import loader
from django.template.defaultfilters import register
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Pembayaran, Spp, Kelas, MetodePembayaran
from .forms import FormPembayaran, FormPembayaranSiswa, FormSpp, FormMetodePembayaran, FormKelas
from .resource import PembayaranResource
from authentication.models import Siswa, Petugas, User

# Check the user role
# def user_check(user):
#     if user.is_siswa:
#         return user.is_siswa
# @user_passes_test(user_check)

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]


@user_passes_test(lambda u: u.is_superuser)
def tambah_kelas(request):
    if request.method == "POST":
        form = FormKelas(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan!")

            return redirect('data-kelas')
    else:
        form = FormKelas()

    return render(request, "administrator/tambah-kelas.html", { "form": form })

@user_passes_test(lambda u: u.is_superuser)
def ubah_kelas(request, id_kelas):
    kelas = Kelas.objects.get(id=id_kelas)
    template = 'administrator/ubah-kelas.html'

    if request.POST:
        form = FormKelas(request.POST, instance=kelas)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")

            return redirect('data-kelas')
    else:
        form = FormKelas(instance=kelas)
        
        context = {
            'form': form,
            'kelas': kelas,
        }
        
    return render(request, template, context)

@user_passes_test(lambda u: u.is_superuser)
def hapus_kelas(request, id_kelas):

    kelas = Kelas.objects.filter(id=id_kelas)
    kelas.delete()
    messages.error(request, "Kelas berhasil dihapus!")
        
    return redirect('data-kelas')

@user_passes_test(lambda u: u.is_superuser)
def data_kelas(request):
    kelas = Kelas.objects.all().order_by('id')

    if request.GET:
        filter_kelas = request.GET.get('filter_kelas', None)
        if filter_kelas:
            kelas = Kelas.objects.filter(nama_kelas=filter_kelas)
        
        
    paginator = Paginator(kelas, 5) # Show 5 kelas per page

    page = request.GET.get('page')
    kelas_paginator = paginator.get_page(page)
    count_kelas_x = Kelas.objects.filter(nama_kelas='X').count()
    count_kelas_xi = Kelas.objects.filter(nama_kelas='XI').count()
    count_kelas_xii = Kelas.objects.filter(nama_kelas='XII').count()

    context = {
        'kelass': kelas_paginator,
        'count_kelas_x': count_kelas_x,
        'count_kelas_xi': count_kelas_xi,
        'count_kelas_xii': count_kelas_xii,
    }
    return render(request, 'administrator/data-kelas.html', context)

@user_passes_test(lambda u: u.is_superuser)
def tambah_mp(request):
    if request.method == "POST":
        form = FormMetodePembayaran(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan!")

            return redirect('data-pembayaran')
    else:
        form = FormMetodePembayaran()

    return render(request, "administrator/tambah-metode-pembayaran.html", { "form": form })

@user_passes_test(lambda u: u.is_superuser)
def tambah_spp(request):
    if request.method == "POST":
        form = FormSpp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan!")

            return redirect('data-pembayaran')
    else:
        form = FormSpp()

    return render(request, "administrator/tambah-spp.html", { "form": form })

@user_passes_test(lambda u: u.is_superuser)
def ubah_mp(request, id_mp):
    metode_pembayaran = MetodePembayaran.objects.get(id=id_mp)
    template = 'administrator/ubah-metode-pembayaran.html'

    if request.POST:
        form = FormMetodePembayaran(request.POST, instance=metode_pembayaran)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")

            return redirect('data-pembayaran')
    else:
        form = FormMetodePembayaran(instance=metode_pembayaran)
        
        context = {
            'form': form,
            'metode_pembayaran': metode_pembayaran,
        }
        
    return render(request, template, context)

@user_passes_test(lambda u: u.is_superuser)
def hapus_mp(request, id_mp):
    metode_pembayaran = MetodePembayaran.objects.filter(id=id_mp)
    metode_pembayaran.delete()
    messages.error(request, "Metode Pembayaran berhasil dihapus!")
        
    return redirect('data-pembayaran')

@user_passes_test(lambda u: u.is_superuser)
def ubah_spp(request, id_spp):
    spp = Spp.objects.get(id=id_spp)
    template = 'administrator/ubah-spp.html'

    if request.POST:
        form = FormSpp(request.POST, instance=spp)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")

            return redirect('data-pembayaran')
    else:
        form = FormSpp(instance=spp)
        
        context = {
            'form': form,
            'spp': spp,
        }
        
    return render(request, template, context)

@user_passes_test(lambda u: u.is_superuser)
def hapus_spp(request, id_spp):
    spp = Spp.objects.filter(id=id_spp)
    spp.delete()
    messages.error(request, "Spp berhasil dihapus!")
        
    return redirect('data-pembayaran')

@user_passes_test(lambda u: u.is_superuser)
def data_pembayaran(request):
    spp = Spp.objects.all().order_by('id')
    metode_pembayaran = MetodePembayaran.objects.all().order_by('id')
        
    paginator_spp = Paginator(spp, 5) # Show 5 spp per page
    paginator_mp = Paginator(metode_pembayaran, 5)

    page = request.GET.get('page')
    page_mp = request.GET.get('page-mp')

    spp_paginator = paginator_spp.get_page(page)
    mp_paginator = paginator_mp.get_page(page_mp)

    context = {
        'spps': spp_paginator,
        'mps': mp_paginator,
    }
    return render(request, 'administrator/data-pembayaran.html', context)

@user_passes_test(lambda u: u.is_staff)
def export_xls(request):
    pembayaran = PembayaranResource()
    dataset = pembayaran.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=laporan-pembayaran-spp.xls'
    return response

@login_required(login_url="/login/")
def list_pembayaran(request):
    if request.user.is_staff:
        pembayaran = Pembayaran.objects.all().order_by('id')

        if request.GET:
            search_query = request.GET.get('search_box', None)
            filter_month = request.GET.get('month', None)
            filter_year = request.GET.get('year', None)
            if search_query:
                pembayaran = Pembayaran.objects.filter(Q(siswa__contains=search_query) | Q(status_pembayaran__contains=search_query) | Q(tgl_bayar__contains=search_query)).order_by('id')
                if pembayaran.count() < 1:
                    messages.error(request, "Data yang dicari tidak ada!")
            if filter_month and filter_year:
                pembayaran = Pembayaran.objects.filter(Q(tgl_bayar__month=filter_month) & Q(tgl_bayar__year=filter_year)).order_by('id')
        
        paginator = Paginator(pembayaran, 5) # Show 5 pembayaran per page

        page = request.GET.get('page')
        pembayarans = paginator.get_page(page)

        context = {
            'pembayarans': pembayarans,
        }
    
    return render(request, "staff/list-pembayaran.html", context)

@login_required(login_url="/login/")
def ubah_pembayaran(request, id_pembayaran):
    pembayaran = Pembayaran.objects.get(id=id_pembayaran)
    template = 'ubah-pembayaran.html'

    if request.user.is_staff:
        template = 'staff/ubah-pembayaran.html'

    if request.POST:
        form = FormPembayaran(request.POST, request.FILES, instance=pembayaran)

        if request.user.is_siswa:
            form = FormPembayaranSiswa(request.POST, request.FILES, instance=pembayaran)

        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")

            if request.user.is_staff:
                return redirect('list-pembayaran')

            return redirect('riwayat-pembayaran')
    else:
        form = FormPembayaran(instance=pembayaran)
        context = {
            'form': form,
            'pembayaran': pembayaran,
        }
        
    return render(request, template, context)

@login_required(login_url="/login/")
def hapus_pembayaran(request, id_pembayaran):
    pembayaran = Pembayaran.objects.filter(id=id_pembayaran)
    pembayaran.delete()
    messages.error(request, "Pembayaran berhasil dihapus!")

    if request.user.is_staff:
        return redirect('list-pembayaran')
        
    return redirect('riwayat-pembayaran')

@login_required(login_url="/login/")
def tambah_pembayaran(request):
    msg     = None
    success = False

    if request.method == "POST":
        form = FormPembayaranSiswa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg     = 'Pembayaran berhasil ditambahkan, tunggu petugas memverifikasi pembayaran anda'
            success = True
        else:
            msg = 'Form is not valid'    
    else:
        form = FormPembayaranSiswa()

    return render(request, "tambah-pembayaran.html", {"form": form, "msg" : msg, "success" : success, })

@login_required(login_url="/login/")
def index(request):
    if request.user.is_authenticated:
        nama = request.user.nama

    pembayaran = Pembayaran.objects.filter(siswa=nama).order_by('-tgl_bayar')[:3]
    pembayaran_in_ascending_order = reversed(pembayaran)
    get_pembayaran_jmlbayar = Pembayaran.objects.filter(Q(status_pembayaran='success') & Q(siswa=request.user.nama))
    months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    
    count_bayar = 0
    list_bayar = []

    for bayar in get_pembayaran_jmlbayar:
        list_bayar.append(bayar.jumlah_bayar)
        count_bayar += bayar.jumlah_bayar

    b = 0
    for e in list_bayar:
        b += e
    n = 0
    o = 0
    for c in list_bayar:
        if c > 1:
            x = c
            list_bayar.remove(c)
            while o < x:
                list_bayar.append(1)
                o += 1
            o = 0
    
    kw = len(list_bayar)
    if kw < 12:
        m = 12 - kw
        while n < m:
            list_bayar.append(0)
            n += 1
    
    list_bayar_dict = dict(zip(months, list_bayar))
    
    pembayaran_ditolak = Pembayaran.objects.filter(Q(status_pembayaran='rejected') & Q(siswa=nama)).count()
    pembayaran_pending = Pembayaran.objects.filter(Q(status_pembayaran='pending') & Q(siswa=nama)).count()
    pembayaran_berhasil = Pembayaran.objects.filter(Q(status_pembayaran='success') & Q(siswa=nama)).count()

    if request.user.is_superuser:
        siswa = User.objects.filter(is_siswa=1).count()
        petugas = User.objects.filter(is_staff=1).count()
        pembayaran_pending = Pembayaran.objects.filter(status_pembayaran='pending').count()
        pembayaran_berhasil = Pembayaran.objects.filter(status_pembayaran='success').count()
        pembayaran_ditolak = Pembayaran.objects.filter(status_pembayaran='rejected').count()
        
        i_month = 1
        pembayaran_month = []
        while i_month <= 12:
            new_pembayaran = Pembayaran.objects.filter(tgl_bayar__month=str(i_month)).count()
            pembayaran_month.append(new_pembayaran)
            i_month += 1
        
        i_year = 2021
        pembayaran_year = []
        while i_year <= 2032:
            new_pembayaran_year = Pembayaran.objects.filter(tgl_bayar__year=str(i_year)).count()
            pembayaran_year.append(new_pembayaran_year)
            i_year += 1

        context = {
            'siswa': siswa,
            'petugas': petugas,
            'pembayaran_pending': pembayaran_pending,
            'pembayaran_berhasil': pembayaran_berhasil,
            'pembayaran_ditolak': pembayaran_ditolak,
            'pembayaran_month': pembayaran_month,
            'pembayaran_year': pembayaran_year,
        }
        return render(request, "administrator/index.html", context)
    elif request.user.is_staff:
        siswa = Siswa.objects.all().count()
        petugas = User.objects.filter(is_staff=1).count()
        pembayaran_pending = Pembayaran.objects.filter(status_pembayaran='pending').count()
        pembayaran_berhasil = Pembayaran.objects.filter(status_pembayaran='success').count()
        
        i_month = 1
        pembayaran_month = []
        while i_month <= 12:
            new_pembayaran = Pembayaran.objects.filter(tgl_bayar__month=str(i_month)).count()
            pembayaran_month.append(new_pembayaran)
            i_month += 1
        
        i_year = 2021
        pembayaran_year = []
        while i_year <= 2032:
            new_pembayaran_year = Pembayaran.objects.filter(tgl_bayar__year=str(i_year)).count()
            pembayaran_year.append(new_pembayaran_year)
            i_year += 1

        context = {
            'siswa': siswa,
            'petugas': petugas,
            'pembayaran_pending': pembayaran_pending,
            'pembayaran_berhasil': pembayaran_berhasil,
            'pembayaran_month': pembayaran_month,
            'pembayaran_year': pembayaran_year,
        }
        return render(request, "staff/index.html", context)

    context = {
        'list_bayar_dict': list_bayar_dict,
        'pembayarans': pembayaran_in_ascending_order,
        'pembayaran_pending': pembayaran_pending,
        'pembayaran_berhasil': pembayaran_berhasil,
        'pembayaran_ditolak': pembayaran_ditolak,
        'months': months,
    }
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def riwayat_pembayaran(request):
    if request.user.is_authenticated:
        nama = request.user.nama
    # pembayaran = Pembayaran.objects.all()
    # filter
    # use __fieldname for sql query INNER JOIN
    # use __contains for sql query LIKE
    # use [:3] for sql query LIMIT
    pembayaran = Pembayaran.objects.filter(siswa=nama).order_by('id')
    paginator = Paginator(pembayaran, 5) # Show 3 pembayaran per page

    page = request.GET.get('page')
    pembayarans = paginator.get_page(page)
    context = {
        'pembayarans': pembayarans,
    }

    return render(request, 'riwayat-pembayaran.html', context)