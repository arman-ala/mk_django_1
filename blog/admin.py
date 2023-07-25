from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title', 'counted_views', 'status', 'published_date')
    empty_value_display = '- - empty - -'
    list_filter = ('status', )
    ordering = ['-created_date']


admin.site.register(Post, PostAdmin)