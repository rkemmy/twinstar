from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from .forms import ProfileForm

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
    form = ProfileForm()
    avatar = Profile.avatar

    return render(request, 'profile.html',{"current_user": current_user,"images": images,"profiles": profiles, "avatar":avatar, "form":format})

def edit_profile(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user_id=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user_profile = form.save()
            user_profile.user = current_user
            user_profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'edit-profile.html', {"form":form})

def explore(request):
    image = Image.objects.all()

    return render(request, 'explore.html', {"image": image})
