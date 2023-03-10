# Generated by Django 4.1.5 on 2023-02-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0019_quizmodel_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstweek_name', models.CharField(blank=True, max_length=40, verbose_name='Жаңа тақырып енгізіңіз')),
                ('firstweek_definition', models.TextField(blank=True, verbose_name='Тақырып сипаттамасы, тапсырмалары')),
                ('comapny_category', models.CharField(blank=True, choices=[('Internet Shop', '3 жас'), ('SuperMarket', '4 жас'), ('Shopping center', '5 жас'), ('Furniture Shop', '6 жас'), ('IT Company', 'Қосымша ақпарат'), ('Educational Center', 'Жаңалықтар')], max_length=40, verbose_name='Қай жасқа арналған')),
            ],
        ),
    ]
