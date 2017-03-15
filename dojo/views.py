from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, x):
    return HttpResponse(int(x) + 10)
