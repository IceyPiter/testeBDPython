# Generated by Django 4.2.5 on 2023-09-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0008_alter_user_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]