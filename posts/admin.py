from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "text")
    list_display = ("title", "text", "created_time")

admin.site.register(Post, PostAdmin)