import json
from django.http import HttpResponse
from django.shortcuts import render


def json_response(request):
    data = {
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }
    json_string = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_string, content_type='application/json')


def mysum(request, numbers):
    def convert_fn(s):
        if s:
            return int(s)
        return 0
    result = sum(map(convert_fn, numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))

