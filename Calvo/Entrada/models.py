from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=20, blank=True)
    login = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.nome

class Mensage(models.Model):
    id = models.AutoField(primary_key=True)
    mensage = models.CharField(max_length=50, blank=True)
    id_user = models.CharField(max_length=3, blank=True)
    key = models.ForeignKey("self", related_name="self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.mensage
