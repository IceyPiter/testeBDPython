from django.contrib import admin
from .models import Mensage, User

# Register your models here.
admin.site.register(User)
admin.site.register(Mensage)