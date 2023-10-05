import smtplib
import email.message
from django.shortcuts import render, redirect
from .models import *
from random import randint

# Create your views here.
def home(request):
    return render(request,'Voleibol.html',{"caso1": "Login", "caso2": "Registrar-se"})

def openUser(request):
    return render(request,'cadastrar_user.html')

def openMsg(request):
    return render(request,'mandar_msg.html')

def openHistory(request):
    return render(request,'Historia.html')

def openFundamentos(request):
    return render(request,'Fundamentos.html')

def openLogin(request):
    return render(request,'realizar_login.html')

def openConf(request):
    return render(request,'configuracao.html', {"caso": 1})

def cadastrar_user(request):
    nomeForm = request.POST.get("user")
    senhaForm = request.POST.get("password")
    emailForm = request.POST.get("mail")

    users = User.objects.all()
    for i in users:
        if i.nome == nomeForm or i.email == nomeForm:
            erro = "!!  Este usuário já existe  !!"
            return render(request, 'cadastrar_user.html', {"erro": erro})
        
    usuario = User(nome=nomeForm,
                password=senhaForm,
                email=emailForm)

    usuario.save()

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
    print(nomeForm)
    print(senhaForm)

    users = User.objects.all()

    for i in users:
        if i.nome == nomeForm or i.email == nomeForm:
            if i.password == senhaForm:
                i.login = True
                i.save()
                return render(request, 'Voleibol.html', {"caso1": i.nome, "caso2": "Configurações"})
        else:
            pass

    return render(request, 'realizar_login.html', {"erro": "Usuário ou Senha Incorretos!!","nome": nomeForm}) 

def deslogar(request, nomeusuario):
    parametro = User.objects.get(nome = nomeusuario)
    if parametro.login == True:
        parametro.login = False
        parametro.save()
        return redirect('/')
    return render(request,'realizar_login.html')

global code

def gerarCode(): 
    code = ""
    for i in range(0,5):
        code += str(randint(0,9))
    return code

def recuperarSenha(request):
    print("A")
    userForm = request.POST.get("nome")
    parametro = User.objects.get(nome = userForm)

    corpo_email = f"""
    Seu código de recuperação é {gerarCode()}
    """
    
    print(parametro.email)
    remetente = "voleiboltccif@gmail.com"
    msg = email.message.Message()
    msg['Subject'] = "Isso é um teste"
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

    return redirect('configuracao/',{"caso":2})
