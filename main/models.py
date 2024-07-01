from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return self.username

class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='services')
    SERVICE_CHOICES = [
    ('haircuts', 'Haircuts and Styling'),
    ('manicure', 'Manicure and Pedicure'),
    ('facial', 'Facial Treatments'),
    ]
    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)

    def __str__(self):
        return f"{self.name} at {self.branch.name}"

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.service.name} at {self.branch.name} on {self.date_time}"

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['branch', 'service', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.none()
        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                self.fields['service'].queryset = Service.objects.filter(branch_id=branch_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['service'].queryset = self.instance.branch.services.all()

class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    star_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.star_rating} stars"
