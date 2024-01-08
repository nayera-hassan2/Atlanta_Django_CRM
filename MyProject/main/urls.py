# main/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from .api_views import (
    QuoteListAPIView,
    ContactUsListAPIView,
    CustomersRecordsListAPIView,
    EmployeesRecordsListAPIView,
    CareerApplicationListAPIView,
)


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
 
  # API endpoints
    path('api/quote/', QuoteListAPIView.as_view(), name='quote-list-api'),
    path('api/contact_us/', ContactUsListAPIView.as_view(), name='contact-us-list-api'),
    path('api/customers_records/', CustomersRecordsListAPIView.as_view(), name='customers-records-list-api'),
    path('api/employees_records/', EmployeesRecordsListAPIView.as_view(), name='employees-records-list-api'),
    path('api/career_application/', CareerApplicationListAPIView.as_view(), name='career-application-list-api'),
]

# path for veiwing image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += [path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT})]