# Generated by Django 4.2.3 on 2023-08-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_bikes_data_fotografia_bikes_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
