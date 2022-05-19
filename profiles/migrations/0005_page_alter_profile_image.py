# Generated by Django 4.0.3 on 2022-05-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(default='data:image/png;base64,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'),
        ),
    ]
