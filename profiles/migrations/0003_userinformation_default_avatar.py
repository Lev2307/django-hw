# Generated by Django 3.1.5 on 2021-07-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210709_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='default_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='default_avatar/'),
        ),
    ]
