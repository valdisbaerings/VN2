from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from templates.user.forms.user_form import CustomUserCreationForm
from templates.user.forms.profile_form import ProfileForm
from user.models import Profile



def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': CustomUserCreationForm()
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html' , {
        'form': ProfileForm(instance=profile)
    })

def profile_picture(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile_picture.html' , {
        'form': ProfileForm(instance=profile)
    })



