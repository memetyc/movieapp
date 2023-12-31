# Generated by Django 4.2.4 on 2023-09-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_comment_tarih'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='slide_img',
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='movies')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
            },
        ),
    ]
