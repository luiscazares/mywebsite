from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # This controls what you see in the "list" view
    list_display = ('thumbnail', 'title', 'order', 'created_at')
    
    # This allows you to click and edit the order directly in the list
    list_editable = ('order',)
    
    # This adds a search bar for your projects
    search_fields = ('title', 'description')

    # A little helper function to show the image in the admin list
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover;" />', obj.image.url)
        return "No Image"
    
    thumbnail.short_description = 'Preview'