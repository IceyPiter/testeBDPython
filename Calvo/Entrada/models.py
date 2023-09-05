from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome