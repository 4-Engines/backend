import smtplib
from email.message import EmailMessage
def send_email_confirm(email,username,id):
    gmail_user =''
    gmail_password = '' 
    msg = EmailMessage()
    msg.set_content('Bienvenido a la plataforma Sigea: '+username+' Para confirmar su cuenta haga click en el siguiente enlace: https://backsigea.herokuapp.com/confirm/'+id)
    msg['Subject'] = 'Bienvenido'
    msg['From'] = ""
    msg['To'] = email
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    

    server.quit()
    return True
def send_email_pass(email,username,password):
    gmail_user =''  
    gmail_password = ''
    msg = EmailMessage()
    msg.set_content('Bienvenido a la plataforma Sigea: '+username+'\n'+'Su contraseña es: '+password)
    msg['Subject'] = 'Bienvenido'
    msg['From'] = ""
    msg['To'] = email
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    







