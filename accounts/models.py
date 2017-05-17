from django.db import models
# from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

