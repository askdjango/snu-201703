from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class LoginForm(AuthenticationForm):
    answer = forms.CharField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data['answer']
        if answer != '6':
            raise forms.ValidationError('땡~!!!')
        return answer


class SignupForm(UserCreationForm):
    phone = forms.CharField()
    address = forms.CharField()

    def save(self):
        user = super().save()

        phone = self.cleaned_data['phone']
        address = self.cleaned_data['address']

        Profile.objects.create(user=user, phone=phone, address=address)

        return user

