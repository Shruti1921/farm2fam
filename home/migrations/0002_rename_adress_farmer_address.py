# Generated by Django 3.2.5 on 2021-10-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmer',
            old_name='adress',
            new_name='address',
        ),
    ]
