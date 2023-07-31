from django.contrib import admin
from .models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact)
admin.site.register(Newsletter)
