from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': post_list,
    })



def post_detail(request, id):
    return HttpResponse('{}번글을 보시겠습니다.'.format(id))

