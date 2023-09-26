import email
from django.shortcuts import render
from .models import User
from .models import Mensage

# Create your views here.
def home(request):
    return render(request,'oqFazer.html')

def openUser(request):
    return render(request,'cadastrar_user.html')

def openMsg(request):
    return render(request,'mandar_msg.html')

def openLogin(request):
    return render(request,'realizar_login.html')

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
