# forms.py

from django import forms
from .models import CustomersRecords

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomersRecords
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'zipcode']
