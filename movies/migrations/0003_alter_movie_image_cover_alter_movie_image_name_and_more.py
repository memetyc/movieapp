# Generated by Django 4.2.4 on 2023-09-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_cover',
            field=models.FileField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.FileField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Gosterimde'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_home',
            field=models.BooleanField(default=False, verbose_name='Anasayfada'),
        ),
    ]
