from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) # For clean URLs like /blog/my-first-post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field('Content', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title