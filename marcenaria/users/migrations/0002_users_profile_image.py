# Generated by Django 5.1.6 on 2025-02-28 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_profile_image.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
