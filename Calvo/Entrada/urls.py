from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cadastrar_user/', views.cadastrar_user, name="cadastrar_user"),
    path('mandar_msg/', views.envia_msg, name="mandar_msg")
]