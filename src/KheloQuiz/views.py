from django.shortcuts import render

def home_view(request):
        return render(request, 'home.html')  

def signup_view(request):
    return render(request, 'signup.html')

def signin_view(request):
    return render(request, 'signin.html')
