# Generated by Django 4.0.3 on 2022-05-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_profile_address_remove_profile_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('image_name', models.TextField()),
                ('user_id', models.CharField(max_length=45)),
            ],
        ),
    ]