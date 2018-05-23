from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image, Profile

# Create your views here.
#@login_required(login_url='/accounts/login/')
def index(request):
    pics = Image.get_all()
    return render(request, 'index.html', {"pics":pics})

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    images = Image.objects.filter(owner_id=request.user)
    profiles = Profile.objects.filter(user=request.user)
    current_user = request.user

    return render(request, 'profile.html',{"current_user": current_user,"images": images,"profiles": profiles})
