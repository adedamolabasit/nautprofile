# Generated by Django 4.0.3 on 2022-05-12 22:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
