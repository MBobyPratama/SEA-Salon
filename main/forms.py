from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Reservation, Review, Branch, Service

class BranchForm(forms.ModelForm):
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Branch
        fields = ['name', 'location', 'opening_time', 'closing_time']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'duration', 'branch']
        widgets = {
            'name': forms.Select(choices=Service.SERVICE_CHOICES),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['branch', 'service', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'star_rating', 'comment']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'first_name', 'last_name')
