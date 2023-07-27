from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     empty_value_display = "no category"


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ('title', 'counted_views', 'status', 'published_date', 'author')
    empty_value_display = '- - empty - -'
    list_filter = ('status', 'author')
    # ordering = ['-created_date']
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)#, CategoryAdmin)
