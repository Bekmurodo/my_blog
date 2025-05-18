from django.contrib import admin
from .models import (Post, Author,
                     PostAuthor,
                     PostReview,
                     Category
                     )



class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "text")
    list_display = ("title", "text", "created_time")

class AuthorAdmin(admin.ModelAdmin):
    pass

class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')

class PostReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(PostAuthor, PostAuthorAdmin)
admin.site.register(PostReview, PostReviewAdmin)
