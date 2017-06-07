from django import forms
from django.core.validators import MinLengthValidator


# def min_length_3_validator(value):
#     if len(value) < 3:
#        raise forms.ValidationError('3글자 이상 입력해주세요.')

min_length_3_validator = MinLengthValidator(3)

