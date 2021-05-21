from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('register', views.register, name="register"),
    path('signout', views.signout, name="signout"),
    path('dashboard/',views.dashboard, name="dashboard")
    
]
