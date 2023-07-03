from django.views.generic import ListView, DetailView
from .models import Author, Post, Comment

class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'
    #queryset = Products.objects.order_by('-id')

class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    contex_object_name = 'author'

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    #queryset = Products.objects.order_by('-id')

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    contex_object_name = 'post'

class CommentList(ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = 'comments'
    #queryset = Products.objects.order_by('-id')

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    contex_object_name = 'comment'