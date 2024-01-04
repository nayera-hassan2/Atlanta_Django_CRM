from django.db import models
from django.utils import timezone


class LoginData(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.timestamp}'


class Quote(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    security_type = models.CharField(max_length=255)
    message = models.TextField()


class ContactUs(models.Model):   
    username = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.username} - {self.email}'
    

class CustomersRecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.TextField()
    state = models.TextField()   
    zipcode = models.TextField() 

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    

class EmployeesRecords(models.Model):
    employee_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class CareerApplication(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    text = models.DateField()  # Assuming this should be a DateField
    address = models.TextField()
    file = models.FileField(upload_to='career_applications/')
    message = models.TextField()

    def __str__(self):
        return f'{self.username} - {self.email}'