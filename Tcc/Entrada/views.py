import smtplib
import email.message
from django.shortcuts import render, redirect
from .models import *
from random import randint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'Voleibol.html',{"caso1": "Login", "caso2": "Registrar-se"})

def homeLogado(request):
    parametro = User.objects.get(nome = nomeuser)
    parametro.login = True
    parametro.save()
    return render(request,'Voleibol.html',{"caso1": nomeuser, "caso2": "Configurações"})

def openUser(request):
    return render(request,'cadastrar_user.html')

def openMsg(request):
    return render(request,'mandar_msg.html')

def openHistory(request):
    return render(request,'Historia.html')

def openFundamentos(request, caso):
    usuario = request.POST.get("Login")
    if usuario == "Login":
        case2 = "Registrar-se"
    else:
        case2 = "Configurações"
    return render(request,'Fundamentos.html', {"caso1": usuario,"caso2": case2, "caso": caso})

@login_required
def openChat(request):
    return render(request,'chat.html')

def openLogin(request):
    return render(request,'realizar_login.html')

def esqueceuSenha(request):
    return render(request,'configuracao.html', {"caso": 1})

def openConf(request):
    return render(request,'configuracao.html', {"caso": 5})

def openRegras(request):
    return render(request,'Regras.html', {"caso": 1})

def cadastrar_user(request):
    nomeForm = request.POST.get("user")
    senhaForm = request.POST.get("password")
    emailForm = request.POST.get("mail")

    users = User.objects.all()
    for i in users:
        if i.username == nomeForm or i.email == nomeForm:
            erro = "!!  Este usuário já existe  !!"
            return render(request, 'cadastrar_user.html', {"erro": erro})
    user = User.objects.create_user(nomeForm, emailForm, senhaForm)

    user.save()

    return render(request, 'Voleibol.html', {"caso1":nomeForm, "caso2": "Configurações"})

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

    user = authenticate(request, username=nomeForm, password=senhaForm)
    if user:
        login(request,user)
        user.save()
        print(request)
    return render(request, 'Voleibol.html', {"caso1": user, "caso2": "Configurações"})

def deslogar(request, nomeusuario):
    logout(request)
    # parametro = User.objects.get(nome = nomeusuario)
    # if parametro.login == True:
    #     parametro.login = False
    #     parametro.save()
        
    #     return redirect('/')
    return render(request,'realizar_login.html')

def gerarCode(): 
    global code
    code = ""
    for i in range(0,5):
        code += str(randint(0,9)) 
    return code
    

def recuperarSenha(request):
    global nomeuser
    userForm = request.POST.get("nome")
    parametro = User.objects.get(nome = userForm)
    nomeuser = userForm

    corpo_email = f"""
    Seu código de recuperação é {gerarCode()}
    """
    
    print(parametro.email)
    remetente = "voleiboltccif@gmail.com"
    msg = email.message.Message()
    msg['Subject'] = "Redeinição de Senha"
    msg['From'] = remetente#'remetente'
    msg['To'] = parametro.email
    password = 'bbfz gjgr cqsy xuuq'#'senha'#nao e a senha do seu email
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    return render(request,'configuracao.html',{"caso":2})

def conferirCode(request):
    codeForm = request.POST.get("code")
        
    if codeForm == code:
       return render(request,'configuracao.html',{"caso":3})
    return render(request,'configuracao.html',{"caso":2,"erro":"Código Incorreto"})

def definirSenha(request):
    codeForm = request.POST.get("code")
    confirmacaoForm = request.POST.get("code2")
    
    parametro = User.objects.get(nome = nomeuser)
    
    if codeForm == confirmacaoForm:
        parametro.password = codeForm
        parametro.save()
        return render(request,'configuracao.html',{"caso":4})
    return render(request,'configuracao.html',{"caso":3,"erro":"Senhas Diferentes"})
        
        

