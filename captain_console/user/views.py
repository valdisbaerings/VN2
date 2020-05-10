import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from templates.user.forms.user_form import CustomUserCreationForm
from templates.user.forms.profile_form import ProfileForm, ProfileUpdateForm
from user.models import Profile, Wishlist, Product


def view_wishlist(request):
    context = {'items': []}
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user_id=request.user.id)
        context["items"] = wishlist
        template = "user/wishlist-index.html"
    return render(request, template, context)


def add_to_wishlist(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        p = json.loads(request.body.decode('utf-8'))
        pid = p["product_id"]
        product = Product.objects.get(id=pid)
        print(product)
        obj = {'product': product, 'user_id': request.user.id}
        wishlist = Wishlist(**obj)
        print(wishlist)
        wishlist.save()
        return JsonResponse({'numberOfItems': Wishlist.objects.filter(user_id=request.user.id).count()})
    return None

def del_from_wishlist(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        cid = c["wishlist_id"]
        Wishlist.objects.get(id=cid).delete()
    return JsonResponse({})



def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': CustomUserCreationForm()
    })

@login_required
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

@login_required
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

@login_required
def update_profile(request): # ATH-ATH-ATH
    if request.method == 'POST':
        form = ProfileUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'user/update_profile.html', {
        'form': ProfileUpdateForm(instance=request.user)
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Error message')
    return render(request, 'user/change_password.html', {
        'form': PasswordChangeForm(request.user)
    })


