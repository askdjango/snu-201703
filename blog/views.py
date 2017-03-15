from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html')

def post_detail(request, id):
    return HttpResponse('{}번글을 보시겠습니다.'.format(id))

