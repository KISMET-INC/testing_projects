from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import _thread

def index(request):
    smtp_server = "smtp.gmail.com"
    port = 587 #For starttls
    password = input("Type your password and press enter:")

    sender_email = "kmoreland909@gmail.com"
    receiver_email = "kmoreland909@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com
    """

    html = """\
    <html>
    <body>
        <h2>Hi,</h2>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.
        </p>
    </body>
    </html>
    """
    part1 = MIMEText(text,'plain')
    part2 = MIMEText(html, 'html')

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    
    def login():
        
        server.starttls(context = context) #Secure the connection
        server.login (sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Success')


    try:
        _thread.start_new_thread(login,())
        
        
        
    except Exception as e:
        print("error sending email")
    finally:
        pass
    return render(request, 'index.html')

# Create your views here.
