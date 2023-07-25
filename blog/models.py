from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey()
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image
    # category = models.ForeignKey()
    # tags = models.ForeignKey()
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"{self.title} - {self.id}"