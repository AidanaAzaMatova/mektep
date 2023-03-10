# Generated by Django 4.1.3 on 2022-12-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0015_videos_company_company_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=True, default='settings.MEDIA_ROOT/logos/1.png', null=True, upload_to='logos/', verbose_name='Сурет орналастыру'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_video',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/logos/earth.mp4', null=True, upload_to='logos/', verbose_name='Видео орналастыру'),
        ),
    ]
