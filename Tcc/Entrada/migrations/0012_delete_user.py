# Generated by Django 4.2.6 on 2023-10-19 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0011_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
