from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def blog_view(request, category_name=None, author_name=None):
    published_posts = Post.objects.filter(status=True)
    selected_posts = []
    if category_name == None and author_name == None:
        context = {
            'published_posts': published_posts,
        }
    elif author_name == None:
        for post in published_posts:
            for cat in post.category.all():
                if category_name == cat.name:
                    selected_posts.append(post)
        context = {
            'published_posts': selected_posts,
        }
    elif category_name == None:
        selected_posts = published_posts.filter(author__username = author_name)
        context = {
            'published_posts': selected_posts,
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


# def blog_category(request, category_name):
#     published_posts = Post.objects.filter(status=True)
#     selected_posts = []
    
#     for post in published_posts:
#         for cat in post.category.all():
#             if category_name == cat.name:
#                 selected_posts.append(post)
#     context = {
#         'published_posts': selected_posts,
#     }
#     return render(request, 'blog/blog-home.html', context)
