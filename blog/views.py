from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, category_name=None, author_name=None):
    published_posts = Post.objects.filter(status=True)
    selected_posts = []
    context = {}
    if author_name == None and category_name != None:
        published_posts = published_posts.filter(category__name = category_name)
                    # context = {
                    #     'published_posts': selected_posts,
                    # }
        # return render(request, 'blog/blog-home.html', context)
    if category_name == None and author_name != None:
        published_posts = published_posts.filter(author__username = author_name)
        # return render(request, 'blog/blog-home.html', context)
    # handling pgination
    try:
        page_number = request.GET.get('page')
        selected_posts = Paginator(published_posts, 2)
        selected_posts = selected_posts.get_page(page_number)
    except PageNotAnInteger:
        selected_posts = selected_posts.get_page(1)
    except EmptyPage:
        selected_posts = selected_posts.get_page(selected_posts.num_pages)
    
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


def blog_search(request):
    selected_posts = []
    if request.method == 'GET':
        published_posts = Post.objects.filter(status=True)
        if search_paramete := request.GET.get('search'):
            selected_posts = published_posts.filter(content__contains=search_paramete)
    context = {
        'published_posts': selected_posts,
    }
    return render(request, 'blog/blog-home.html', context)


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
