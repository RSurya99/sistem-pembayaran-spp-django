# Generated by Django 2.2.12 on 2021-04-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_siswa_id_spp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile/'),
        ),
    ]
