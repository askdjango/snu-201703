import os
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import get_nametag_file


def image_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'flower.jpg')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


def json_response(request):
    data = {
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }
    # json_string = json.dumps(data, ensure_ascii=False)
    # return HttpResponse(json_string, content_type='application/json')
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def mysum(request, numbers):
    def convert_fn(s):
        if s:
            return int(s)
        return 0
    result = sum(map(convert_fn, numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def nametag(request, name):
    f = get_nametag_file(name)
    return HttpResponse(f, content_type='image/png')

