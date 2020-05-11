from django.contrib.auth import login
from django.shortcuts import render, redirect
from templates.admin.forms.login_form import AdminAuthenticationForm


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        form = AdminAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('admin_home')
    else:
        form = AdminAuthenticationForm()
    return render(request,'admin/admin_login.html', {
        'form': form
    })

def admin_home(request):
    return render(request, 'admin/index.html')






