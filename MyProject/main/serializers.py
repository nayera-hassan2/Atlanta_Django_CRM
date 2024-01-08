# main/serializers.py
from rest_framework import serializers
from .models import Quote, ContactUs, CustomersRecords, EmployeesRecords, CareerApplication

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class CustomersRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomersRecords
        fields = '__all__'

class EmployeesRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesRecords
        fields = '__all__'

class CareerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerApplication
        fields = '__all__'
