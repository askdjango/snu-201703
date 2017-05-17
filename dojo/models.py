import re
from django import forms
from django.conf import settings
from django.db import models

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise forms.ValidationError('Invalid LngLat Value')

class Post(models.Model):
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
            validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    test_field = models.IntegerField(default=10)

    def __str__(self):
        return self.title

