# Generated by Django 4.2.4 on 2023-09-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_comment_tarih'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tarih',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]