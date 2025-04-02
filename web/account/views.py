from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


def login_request(request):

    if request.user.is_authenticated:
        return render(request, "index")
    if request.method == "POST":
        username = request.POST["username"] 
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "account/login.html", {
            "error":"username ya da sifre yalnisdir"
        })
            
    else:
        return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        # register
        pass
    else:
        return render(request, "account/register.html")

def logout_request(request):
    return redirect("products")

