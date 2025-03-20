from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def reset_password(request):
    return render(request, 'resetpassword.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def history(request):
    return render(request, 'history.html')

def about(request):
    return render(request, 'about.html')

def setting(request):
    return render(request, 'setting.html')


    
