# Generated by Django 3.1.6 on 2021-06-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0007_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile_photos'),
        ),
    ]
