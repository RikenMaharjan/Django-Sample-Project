# Generated by Django 3.2.1 on 2021-05-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='user/'),
        ),
    ]
