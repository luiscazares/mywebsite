from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    prepopulated_fields = {'slug': ('title',)} # Automatically fills slug based on title
    list_filter = ('published', 'author')
    search_fields = ('title', 'content')