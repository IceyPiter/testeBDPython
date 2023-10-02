import email
from django.shortcuts import render
from .models import *

global NumCaso
NumCaso = 1

# Create your views here.
def home(request):
    if NumCaso == 1:
        caso1 = "Login"
        caso2 = "Registrar-se"
        NumCaso += 1
    return render(request,'Voleibol.html',{"caso1": caso1, "caso2": caso2})

def openUser(request):
    return render(request,'cadastrar_user.html')

def openMsg(request):
    return render(request,'mandar_msg.html')

def openLogin(request):
    return render(request,'realizar_login.html',{"meunome": "Pedro"})

def cadastrar_user(request):
    nomeForm = request.POST.get("user")
    senhaForm = request.POST.get("password")
    emailForm = request.POST.get("mail")

    usuario = User(nome=nomeForm,
                password=senhaForm,
                email=emailForm)

    usuario.save()

    usuarios = User.objects.all()
    users = {"user": usuarios}

    return render(request, 'listUser.html', users)

def envia_msg(request):
    mensagemForm = request.POST.get("msg")
    idUser = request.POST.get("ID")

    mensagem = Mensage(mensage=mensagemForm,
                        id_user=idUser)

    mensagem.save()

    mensagens = Mensage.objects.all()
    mensages = {"msg": mensagens}

    return render(request, 'listUser.html', mensages)

def realizar_login(request):
    nomeForm = request.POST.get("name")
    senhaForm = request.POST.get("password")

    users = User.objects.all()
    teste = {"content": users}

    if nomeForm in teste["content"]:
        teste = [nomeForm]
    

    return render(request, 'listUser.html', teste)
