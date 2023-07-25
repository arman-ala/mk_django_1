from django.shortcuts import render
from blog.models import Post


def blog_view(request):
    published_posts = Post.objects.filter(status=True)
    context = {
        'published_posts': published_posts,
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    return render(request, 'blog/blog-single.html')
