# Generated by Django 4.0.3 on 2022-05-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_about_alter_profile_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.TextField(default='https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png'),
        ),
    ]
