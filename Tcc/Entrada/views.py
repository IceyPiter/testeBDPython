import email
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'Voleibol.html',{"caso1": "Login", "caso2": "Registrar-se"})

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

    # usuarios = User.objects.all()
    # users = {"user": usuarios}

    return render(request, 'Voleibol.html')

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
    print(nomeForm)
    print(senhaForm)

    users = User.objects.all()

    for i in users:
        if i.nome == nomeForm or i.email == nomeForm:
            if i.password == senhaForm:
                i.login = True
                i.save()
                return render(request, 'Voleibol.html', {"caso1": nomeForm, "caso2": "Configurações"})
        else:
            pass

    return render(request, 'realizar_login.html', {"erro": "Usuário ou Senha Incorretos!!"})
    

    
