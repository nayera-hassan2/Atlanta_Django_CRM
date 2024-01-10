# forms.py

from django import forms
from .models import CustomersRecords

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomersRecords
        fields = '__all__'
