# Generated by Django 4.1.5 on 2023-01-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollingapiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='User',
            new_name='User_C',
        ),
    ]
