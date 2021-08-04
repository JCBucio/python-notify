import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import smtplib
import socket

def message(subject="Python Notification", text="", img=None, attachment=None):
    # Crea el contenido del mensaje
    msg = MIMEMultipart()
    msg['Subject'] = subject    # Agrega el asunto
    msg.attach(MIMEText(text))  # Agrega el texto del contenido

    # Revisa si tenemos una entrada en el parámetro img
    if img is not None:
        # Si tenemos una entrada accesamos a ella y revisamos que sea una lista
        if type(img) is not list:
            img = [img] # Si no es una lista la volvemos una
        
        # Ahora nos movemos a través de la lista
        for one_img in img:
            img_data = open(one_img, 'rb').read()   # Se leen los datos binarios de la imagen
            
            # Se agregan los datos de la imagen a MIMEMultipart usando MIMEImage,
            # le agregamos el nombre de archivo usando os.basename
            msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))
    
    # Hacemos lo mismo que realizamos en imágenes para los archivos adjuntos
    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]

        for one_attachment in attachment:
            with open(one_attachment, 'rb') as f:
                # Se lee el documento adjunto con MIMEApplication
                file = MIMEApplication(
                    f.read(),
                    name = os.path.basename(one_attachment)
                )
            # Se editan los metadatos de los archivos adjuntos
            file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
            msg.attach(file)    # Finalmente añadimos los archivos adjuntos al mensaje
    
    return msg


def send(msg, server='smtp.gmail.com', port='587'):
    # Se intenta el siguiente código dentro de un bloque try-except en caso de una falla en la red
    try:
        # Inicia una conexión con el servidor seleccionado de email
        smtp = smtplib.SMTP (server, port)
        # Este es el comando 'Extended Hello', realiza un 'saludo' al servidor SMTP o ESMTP
        smtp.ehlo()
        # Ésta es la línea del comando 'Start Transport Layer Security', nos dice que el servidor
        # se estará comunicando con una encriptación TLS
        smtp.starttls()

        # Se leen el email y la contraseña de archivos de texto separados en el directorio /data
        with open('../data/email.txt', 'r') as fp:
            email = fp.read()
        with open('../data/pwd.txt', 'r') as fp:
            pwd = fp.read()
        
        # Se inicia sesión en el servidor
        smtp.login(email, pwd)
        # Se envía la notificación al mismo correo
        # Si se quiere enviar a otro destinatario se debe de especificar el correo en lugar 
        # del segundo parámetro de 'email'
        smtp.sendmail(email, email, msg.as_string())
        # Se cierra la sesión
        smtp.quit()
    except socket.gaierror:
        print("\n Network connection error, mail not sent. \n") 