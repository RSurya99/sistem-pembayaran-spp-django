# Generated by Django 2.2.12 on 2021-03-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210329_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembayaran',
            name='status_pembayaran',
            field=models.CharField(choices=[('pending', 'Menunggu Verifikasi'), ('done', 'Pembayaran Berhasil')], default='pending', max_length=50),
        ),
        migrations.DeleteModel(
            name='StatusPembayaran',
        ),
    ]
