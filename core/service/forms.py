from django import forms
from .models import Service

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['customer_name', 'phone_number', 'device_name', 'customer_mail', 'customer_type', 'submitted_price', 'device_state', 'device_problem']