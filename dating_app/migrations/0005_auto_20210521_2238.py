# Generated by Django 3.1.6 on 2021-05-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0004_auto_20210521_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('', 'Unspecified')], default='M', max_length=1),
        ),
    ]
