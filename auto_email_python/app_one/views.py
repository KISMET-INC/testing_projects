from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import smtplib, ssl
from smtplib import SMTPException

def index(request):
    smtp_server = "smtp.gmail.com"
    port = 587 #For starttls
    sender_email = "kmoreland909@gmail.com"
    password = input("Type yoru password")
    receiver_email = "kmoreland909@gmail.com"
    message = """\
        Subject: Hi
        This is a message from Python
    """

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context = context) #Secure the connection
        server.login (sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Success')
    except Exception as e:
        print("error sending email")
    finally:
        server.quit()
    return render(request, 'index.html')

# Create your views here.
