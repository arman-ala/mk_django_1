from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-latest_posts.html')
def latest_posts():
    published_posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts': published_posts}


@register.inclusion_tag('blog/blog-posts_categories.html')
def posts_categories():
    categories = Category.objects.all()
    return {'categories': categories}
