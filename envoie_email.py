import smtplib,ssl
from email.message import EmailMessage
class envoie_email():
    def __init__(self, message):
        self.message = message
        smtp_address= "smtp.gmail.com"
        smtp_port=465

        email_address = "cantine.arbis@gmail.com"
        email_password = "cantine@ladaux33760"

        email_receiver= "l.cavaleiro@hotmail.fr"

        context= ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            # connexion au compte
            server.login(email_address, email_password)
            # envoi du mail
            server.sendmail(email_address, email_receiver, self.message)


