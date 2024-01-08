# main/api_views.py
from rest_framework import generics
from .models import Quote, ContactUs, CustomersRecords, EmployeesRecords, CareerApplication
from .serializers import QuoteSerializer, ContactUsSerializer, CustomersRecordsSerializer, EmployeesRecordsSerializer, CareerApplicationSerializer

class QuoteListAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class ContactUsListAPIView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class CustomersRecordsListAPIView(generics.ListCreateAPIView):
    queryset = CustomersRecords.objects.all()
    serializer_class = CustomersRecordsSerializer

class EmployeesRecordsListAPIView(generics.ListCreateAPIView):
    queryset = EmployeesRecords.objects.all()
    serializer_class = EmployeesRecordsSerializer

class CareerApplicationListAPIView(generics.ListCreateAPIView):
    queryset = CareerApplication.objects.all()
    serializer_class = CareerApplicationSerializer
