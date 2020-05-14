import json
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from templates.user.forms.user_form import CustomUserCreationForm
from templates.user.forms.profile_form import ProfileForm, ProfileUpdateForm
from user.models import Profile, Wishlist, Product, Review
from user.forms.create_review import ReviewCreateForm
from order.views import OrderItem, Order

@login_required
def get_my_orders(request):
    context = {'items': []}
    if request.user.is_authenticated:
        order = Order.objects.filter(user_id=request.user.id)
        order_item = OrderItem.objects.all()
        products = Product.objects.all()
        context["items"] = order_item
        context["orders"] = order
        context["products"] = products
        template = "user/get_my_orders.html"
    return render(request, template, context)

@login_required
def get_my_reviews(request):
    context = {'items': []}
    if request.user.is_authenticated:
        review = Review.objects.filter(user_id=request.user.id)
        context["items"] = review
        template = "user/get_my_reviews.html"
    return render(request, template, context)


def review_index(request, id):
    if request.method == "POST":
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('products', id=id)
    else:
        form = ReviewCreateForm()
    return render(request, 'user/review_index.html', {
        'form': form,
        'id': id
    })


def add_review(request, id):
    print(request.is_ajax())
    print(request.method == "POST")
    print(request.user.is_authenticated)
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        p = json.loads(request.body.decode('utf-8'))
        pid = p["product_id"]
        prev = p["review"]
        product = Product.objects.get(id=pid)
        obj = {'product': product, 'user_id': request.user.id, 'review': prev}
        review = Review(**obj)
        review.save()
        return JsonResponse({'numberOfItems': Review.objects.filter(user_id=request.user.id).count()})
    elif request.user.is_authenticated == False:
        return HttpResponse(status=404)



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
    elif request.user.is_authenticated == False:
        return HttpResponse(status=404)
    return None


@login_required
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
    return render(request, 'user/profile_picture.html', {
        'form': ProfileForm(instance=profile)
    })


@login_required
def update_profile(request):  # ATH-ATH-ATH
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

