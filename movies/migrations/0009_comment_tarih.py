# Generated by Django 4.2.4 on 2023-09-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_comment_email_alter_comment_ratting'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tarih',
            field=models.DateField(null=True),
        ),
    ]