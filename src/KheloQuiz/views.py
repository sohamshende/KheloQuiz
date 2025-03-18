from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  

def signup_view(request):
    return render(request, 'signup.html')

def signin_view(request):
    return render(request, 'signin.html')

def reset_password(request):
    return render(request, 'resetpassword.html')

def dashboard(request):
    return render(request, 'dashboard.html')
