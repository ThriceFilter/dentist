from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        #send and email
        send_mail(
            fullname, # subject
            message, # message
            ["squid@email.com"], # from email
            email,)

        render(request, 'contact.html', {'fullname': fullname})
    return render(request, 'contact.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def about(request):
    return render(request, 'about.html', {})

def news(request):
    return render(request, 'news.html', {})

def services(request):
    return render(request, 'services.html', {})

def index(request):
    return render(request, 'index.html', {})
