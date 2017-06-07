from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):
    phone = forms.CharField()
    address = forms.CharField()

    def save(self):
        user = super().save()

        phone = self.cleaned_data['phone']
        address = self.cleaned_data['address']

        Profile.objects.create(user=user, phone=phone, address=address)

        return user

