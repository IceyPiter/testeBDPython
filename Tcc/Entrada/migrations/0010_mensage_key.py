# Generated by Django 4.2.5 on 2023-10-02 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0009_alter_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensage',
            name='key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='self', to='Entrada.mensage'),
        ),
    ]
