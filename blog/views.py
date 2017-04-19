from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        post_list = post_list.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'q': q,
        'post_list': post_list,
    })


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

