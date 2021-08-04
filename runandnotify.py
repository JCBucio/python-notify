import mail_notify
import subprocess
import time

# Se ejecuta el comando deseado con subprocess.run()
subprocess.run('python initialize.py', shell=True)

# Checkpoint para revisar que el comando haya sido ejecutado correctamente
print("\n ##### FIRST TASK COMPLETE ##### \n")
time.sleep(3)
print("Processing data...")

# Se escribe el standard output dentro de un archivo de texto llamado log.txt
with open('log.txt', 'w') as f:
    p1 = subprocess.run('python backfill.py -v -s 2004-09-15 -e 2004-09-16', 
    shell=True, 
    stdout=f, 
    text=True)

# Se crea el objeto para darle formato al correo que notificará que el programa ha sido
# ejecutado de manera exitosa
msg = mail_notify.message(
    subject="REDPy run finished",
    text="Your data is ready to be used.",
    attachment='log.txt'
)

# Se llama la función mail_notify.send() del script mail_notify.py con el parámetro del nuevo mensaje
mail_notify.send(msg)

# Output a la terminal para revisar que el script haya sido ejecutado exitosamente
print("\n ##### ALL TASKS COMPLETED SUCCESFULLY ##### \n")