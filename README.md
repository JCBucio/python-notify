# Python notify

Este es un programa que crea un correo electrónico y lo envía a través del servidor de correo preferido
para notificar cuando un proceso ha sido completado en la terminal corriendo los comandos desde python.

El correo tiene formato incluyendo destinatario, asunto, contenido, imágenes y archivos adjuntos.
Al programa se le pueden añadir más parámetros para enviar correos con reportes en excel o con gráficas del proceso llevado a cabo, 
también es conveniente para hacer un seguimiento en el procesamiento de grandes cantidades de datos.

El programa utiliza las siguientes librerías:
- `os`
- `subprocess`
- `time`
- `email.mime`
- `smtplib`
- `socket`

Dentro de `mail_notify.py` se encuentran las funciones para darle formato al correo y para iniciar sesión en el servidor.
Para iniciar sesión es necesario añadir 2 archivos de texto en un directorio llamado 'data' dentro de tu directorio con tu proyecto,
uno de los archivos se llamará `email.txt` y contendrá el correo desde el cual se enviará el mensaje, el segundo archivo se llamará
`pwd.txt` y en él se encontrará la contraseña del correo al cual se quiere acceder.

### Importante: *Nunca subas los archivos con tu correo y contraseña a tus repositorios de Github*

Con el siguiente comando puedes correr el código:
```bash
python runandnotify.py
```
Si nuestra tarea es bastante larga podemos correrla en background con un `&` al final del comando
