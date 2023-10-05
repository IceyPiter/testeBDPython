import smtplib
import email.message

def enviar_email(destinatario):  
    corpo_email = """
    Ouvi dizer que o Rodrigo é calvo
    """

    remetente = "voleiboltccif@gmail.com"
    msg = email.message.Message()
    msg['Subject'] = "Isso é um teste"
    msg['From'] = remetente#'remetente'
    msg['To'] = destinatario#'destinatario1', 'destinatario2', etc.
    password = 'bbfz gjgr cqsy xuuq'#'senha'#nao e a senha do seu email
    
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email("rodrigojrsouzaavelar@gmail.com")