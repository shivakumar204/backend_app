from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('share/', views.share_snippet, name='share_snippet'),
]

