# shop/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # logout을 추가합니다.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404 # get_object_or_404를 추가합니다.
from .models import Product

def landing_page(request):
    products = Product.objects.all()
    return render(request, 'shop/landing.html', {'products': products})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                return render(request, 'shop/login.html', {'form': form, 'error_message': '잘못된 사용자명 또는 비밀번호입니다.'})
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

# 로그아웃 기능 추가
def logout_user(request):
    logout(request)
    return redirect('landing_page')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})