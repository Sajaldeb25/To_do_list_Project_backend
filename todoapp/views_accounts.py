from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "Username and password is invalid."
            }
            return render(request, "accounts/login.html", context=context)
        else:
            login(request, user)
            return redirect('/')
    return render(request, "accounts/login.html", {})


def logout_view(request):
    return render(request, "accounts/logout.html", {})


def register_view(request):
    return render(request, "accounts/register.html", {})



