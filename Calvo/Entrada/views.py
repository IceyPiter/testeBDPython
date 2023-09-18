import email
from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request,'teste.html')

def cadastrar_user(request):
    nomeForm = request.POST.get("user")
    senhaForm = request.POST.get("password")
    emailForm = request.POST.get("mail")

    usuario = User(nome=nomeForm,
                password=senhaForm,
                email=emailForm)

    usuario.save()

    return render(request, 'listUser.html', {"usuario": usuario})