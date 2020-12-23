from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def index(request):
    smtp_server = "smtp.gmail.com"
    port = 587 #For starttls
    password = "Passion12**"
    
    sender_email = "kmoreland909@gmail.com"
    receiver_email = "kmoreland909@gmail.com"


    message = """From: Pets Connect <from@fromdomain.com>
To: Kristen <to@todomain.com>
Subject: Someone sent love to Poe!

Sign in to see who.
<b>This is HTML message.</b>
<h1>This is headline.</h1>
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
