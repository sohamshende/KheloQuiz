from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})

def auth_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/signup.html", {"form" :form})

