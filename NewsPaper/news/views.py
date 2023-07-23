from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from django.utils import timezone

class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = ['-time_in']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now())  # добавим переменную текущей даты time_now
        context[
            'value1'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news/new.html'
    context_object_name = 'post'