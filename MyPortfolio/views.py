from django.contrib import messages
from .models import Home, About, Profile, Category, Skills, Portfolio
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def index(request):
    # Home
    home = Home.objects.latest('updated')

    # about
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # skills
    categories = Category.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
    }

    return render(request, 'index.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            send_mail(
                'Message from Portfolio Contact Form',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                email,  # sender's email address
                ['zendielsingano@gmail.com'],  # recipient's email address
                fail_silently=False,
            )
            return HttpResponse('Your message has been sent successfully.')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})