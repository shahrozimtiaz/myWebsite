from django.shortcuts import render, redirect, reverse
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class emailSender:
    # sender_email = ''
    # password = ''
    # receiver_email = ''
    # subject = ''
    # text = ''
    # message = None

    def __init__(self,sender_email,password):
        self.sender_email = sender_email
        self.password = password
        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context)
        self.username = sender_email.split("@")[0]
        self.server.login(self.username, self.password)

    def sendMessage(self,receiver_email,subject,text):
        self.receiver_email = receiver_email
        self.subject = subject
        self.text = text
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = self.subject
        body = MIMEText(text, "plain")
        self.message.attach(body)
        self.server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())

    def close(self):
        self.server.close()
        print("Good bye")

def home(request):
    return render(request, 'myWebsite/home.html')

def projects(request):
    return render(request, 'myWebsite/projects.html')

def courseWork(request):
    return render(request, 'myWebsite/courseWork.html')

def contact(request):
    if request.POST:
        email_sender = emailSender('shahrozautomation@gmail.com', 'automation123')
        email_sender.sendMessage('shahrozimtiaz07@gmail.com', request.POST.get('subject'),'Automated Personal Website Message:\nEmail: {} \nName: {} \nSubject: {} \nMessage: {}'.format(request.POST.get('email'),request.POST.get('name'), request.POST.get('subject'),request.POST.get('message')))
        email_sender.close()
        return redirect(reverse('myWebsite:sent'))
    return render(request, 'myWebsite/contact.html')

def sent(request):
    return render(request, 'myWebsite/sent.html')