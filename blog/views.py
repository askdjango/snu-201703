from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import F
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
    Post.objects.filter(id=id).update(hits=F('hits')+1)
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

