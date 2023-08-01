from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-latest_posts.html')
def latest_posts():
    published_posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': published_posts}


@register.inclusion_tag('blog/blog-posts_categories.html')
def posts_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    categories_dict = {}
    
    for cat in categories:
        categories_dict[cat] = posts.filter(category=cat).count()
    
    return {'categories': categories_dict}
