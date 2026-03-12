from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(published=True).order_by('-created_at')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
