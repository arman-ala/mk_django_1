from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(request):
    published_posts = Post.objects.filter(status=True)
    context = {
        'published_posts': published_posts,
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    published_posts = Post.objects.filter(status=True)
    post = get_object_or_404(published_posts, pk=pid)

    # post = get_object_or_404(Post, pk=pid, status=True)
    context = {
        "post": post,
    }
    return render(request, 'blog/blog-single.html', context)
