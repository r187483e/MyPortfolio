from django.contrib import messages
from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio
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

def simple_mail(request):
    send_mail(message=f"{'message'}")
