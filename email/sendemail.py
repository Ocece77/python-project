from email.message import EmailMessage
from pw import password
import smtplib ,ssl


# Information about our account 
email_sender = "oceanekasindupro@gmail.com"
email_password = password

# Information about the receiver 
email_receiver = "tracy.kasindu@gmail.com"

# The mail subject and message 
subject = "Tarte au pomme ! "
body="""
C'est le body de notre message  !!
 """


# Information about our account 
em = EmailMessage()
em["From"] = email_sender
em['To'] = email_receiver
em["subject" ] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com" ,465, context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())