from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    def convert_fn(s):
        if s:
            return int(s)
        return 0
    result = sum(map(convert_fn, numbers.split("/")))
    return HttpResponse(result)

