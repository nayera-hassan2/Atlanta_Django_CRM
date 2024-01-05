# main/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve


app_name = 'main'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('get_a_quote/', views.get_a_quote, name='get_a_quote'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_us_records/', views.contact_us_records, name='contact_us_records'),
    path('get_a_quote_records/', views.get_a_quote_records, name='get_a_quote_records'),
    path('career/', views.career, name='career'),
    path('career_records/', views.career_records, name='career_records'),
    path('customer_records/', views.customer_records, name='customer_records'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    
    path('employees_records/', views.employees_records, name='employees_records'),
 
]

# path for veiwing image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += [path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT})]