from django.db import models

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