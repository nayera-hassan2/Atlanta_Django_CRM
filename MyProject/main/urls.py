# main/urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('get_a_quote/', views.get_a_quote, name='get_a_quote'),
    path('contact_us/', views.contact_us, name='contact_us'),
]