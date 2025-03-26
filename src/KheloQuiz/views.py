from django.shortcuts import render

def home(request):
    return render(request, 'layouts/welcome_screen.html')  





    
