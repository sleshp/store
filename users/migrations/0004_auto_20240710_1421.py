# Generated by Django 3.2.13 on 2024-07-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240710_1400'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailVerified',
            new_name='EmailVerification',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
    ]
