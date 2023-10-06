from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class MyView(PermissionRequiredMixin, View):
    permission_required = ('news.view_Post',
                           'news.add_Post',
                           'news.delete_Post',
                           'news.change_Post')
class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = ['-time_in']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] =  PostFilter(self.request.GET, queryset=self.get_queryset())
        context['choices'] = Post.POST_TYPES
        context['form'] = PostForm()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

class PostDetailView(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()

class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', )
    template_name = 'news/post_create.html'
    form_class = PostForm

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', )
    template_name = 'news/post_create.html'
    form_class = PostForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    sucess_url = reverse_lazy('news:posts')
class PostDetail(DetailView):
    model = Post
    template_name = 'news/new.html'
    context_object_name = 'post'

class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-time_in')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts
        }

        return render(request, 'news/news.html', data)