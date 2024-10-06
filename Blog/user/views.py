from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from .models import MyUser


# Create your views here.
def registration_page(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = MyUser.objects.filter(username=username, email=email).exists()
        if not user:
            user = MyUser.objects.create_user(username=username,email=email,password=password)
            user.save()
            return JsonResponse({'redirect_url': '/'})
        else:
            return JsonResponse({'error': 'This user is already used'})

    return render(request, "registration.html")

def login_page(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = MyUser.objects.filter(username=username).exists()
        if user:
            user = MyUser.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return JsonResponse({'redirect_url': '/'})
        else:
            return JsonResponse({'error': 'Name or password is incorrect'})
            
    return render(request, "login.html")