from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)  # Fixed
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  # first time creation 
    updated_at = models.DateTimeField(auto_now=True)  # when data is modified 
    
    def __str__(self):
        return self.first_name
