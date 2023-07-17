from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'templates/news/news.html'
    context_object_name = 'posts'