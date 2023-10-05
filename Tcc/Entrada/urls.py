from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('openUser/', views.openUser, name="openUser"),
    path('openHistory/', views.openHistory, name="openHistory"),
    path('openFundamentos/', views.openFundamentos, name="openFundamentos"),
    path('openMsg/', views.openMsg, name="openMsg"),
    path('openLogin/', views.openLogin, name="openLogin"),
    path('mandar_msg/', views.envia_msg, name="mandar_msg"),
    path('cadastrar_user/', views.cadastrar_user, name="cadastrar_user"),
    path('realizar_login/', views.realizar_login, name="realizar_login"),
    path('deslogar/<str:nomeusuario>', views.deslogar, name="deslogar"),
    path('recuperarSenha/', views.recuperarSenha, name="recuperarSenha"),
]