# Generated by Django 2.2.12 on 2021-03-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210329_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembayaran',
            name='id_siswa',
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='siswa',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
