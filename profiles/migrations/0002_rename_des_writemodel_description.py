# Generated by Django 4.2.6 on 2023-12-22 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writemodel',
            old_name='des',
            new_name='description',
        ),
    ]
