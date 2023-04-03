import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('saralavallabhapuram800@gmail.com','dfsceevtpgikblpo')
    msg=EmailMessage()
    msg['From']='saralavallabhapuram800@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
