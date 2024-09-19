from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:short_url>/', views.redirect_short_url, name='redirect'),

]
