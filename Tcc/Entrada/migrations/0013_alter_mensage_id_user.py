# Generated by Django 4.2.5 on 2023-10-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0012_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensage',
            name='id_user',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
