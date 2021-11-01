<h1 align="center">Sistem Pembayaran SPP Berbasis Web </h1>
<p align="center">sebuah aplikasi berbasis web yang saya buat untuk tugas ujikom dan sebagai salah satu syarat untuk kelulusan.</p>

<center>

![Tampilan antarmuka Aplikasi](/staticfiles/interface.png)
![version](https://img.shields.io/badge/version-1.0-blue.svg)

</center>

## Cara Penginstalan
1. Clone repo ini terlebih dahulu
```bash
git clone https://github.com/RSurya99/aplikasi-pembayaran-spp
```
2. Buat virtual environment
```bash
pip install virtualenv
virtualenv env
```
3. Install semua module yang dibutuhkan
```bash
pip3 install -r requirements.txt
```
4. Run aplikasi terlebih dahulu (untuk membuat file sqlite) lalu migrate all
```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```
5. Buat file .env di root folder dan copy text berikut
```bash
DEBUG=True/False
SECRET_KEY=YOUR_SECRET_KEY
EMAIL=YOUR_EMAIL
EMAILPASSWORD=YOUR_EMAIL_PASSWORD
```
<small>catatan: email dan password email dibutuhkan untuk melakukan koneksi dengan server smtp gmail.</small>

6. Run kembali aplikasi nya
```bash
python manage.py runserver
```

## Donasi

Jika kamu telah menggunakan project ini dan itu berguna untuk kamu, mohon pertimbangkan untuk melakukan donasi:

[Ko-fi](https://ko-fi.com/rsurya99) | [Trakteer](https://trakteer.id/rsurya99)

## Lisence

This project is under MIT license
