# Generated by Django 4.1 on 2022-08-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]