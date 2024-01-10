# main/api_views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Quote, ContactUs, CustomersRecords, EmployeesRecords, CareerApplication
from .serializers import QuoteSerializer, ContactUsSerializer, CustomersRecordsSerializer, EmployeesRecordsSerializer, CareerApplicationSerializer

class QuoteListAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'message': 'List of quotes retrieved successfully.', 'data': response.data}
        return response
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data= {'message': 'Quote created successfully.', 'data': response.data}
        return response

class ContactUsListAPIView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data= {'message': 'List of contact us entries retrieved successfully.', 'data': response.data}
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Contact us entry created successfully.','data': response.data}
        return response

class CustomersRecordsListAPIView(generics.ListCreateAPIView):
    queryset = CustomersRecords.objects.all()
    serializer_class = CustomersRecordsSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'message': 'List of Customer entries retrieved successfully.', 'data': response.data}
        return response
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Customer entry created successfully.', 'data': response.data}
        return response


class EmployeesRecordsListAPIView(generics.ListCreateAPIView):
    queryset = EmployeesRecords.objects.all()
    serializer_class = EmployeesRecordsSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'message': 'List of Employee entries retrieved successfully.', 'data': response.data}
        return response
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Employee entry created successfully.', 'data': response.data}
        return response

class CareerApplicationListAPIView(generics.ListCreateAPIView):
    queryset = CareerApplication.objects.all()
    serializer_class = CareerApplicationSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'message': 'List of Career entries retrieved successfully.', 'data': response.data}
        return response
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Career entry created successfully.', 'data': response.data}
        return response
