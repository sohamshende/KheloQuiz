from django.urls import path, include
from .views import auth_view,home_view
urlpatterns = [
    
    path('signup/', auth_view, name="auth_view"),
    path("accounts/", include("django.contrib.auth.urls")),

]