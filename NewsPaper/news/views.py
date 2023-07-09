from django.views.generic import ListView, DetailView
from .models import Author, Post, Comment
from django.shortcuts import render
from django.core.paginator import Paginator
from .filters import random_Filter, custom_filters
from .forms import PostForm

class PostUpdateView(UpdateView):
    template_name = 'news/templates/news_create.html'
    form_class = PostForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
class ProductDeleteView(DeleteView):
    template_name = 'news/templates/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'
    paginate_by = 1
   # form_class = PostForm

    def get(self, request):
        Authors = Author.objects.order_by('name')
        p = Paginator(Authors, 10)
        Authors = p.get_page(request.GET.get('page', 10)

        data = {
            'Authors': Authors,
        }
        return render(request, 'news/templates/news.html', data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_Filter'] = AuthorFilter(self.request.GET, queryset=self.get_queryset())
        return context

    class PostDetailView(DetailView):
        template_name = 'news/news_detail.html'
        queryset = Post.objects.all()
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        #Author = request.POST['Author']
       # zagolovok = request.POST['zagolovok']
       # comment = request.POST['comment']
        #date = request.POST['date']

        #product = Product(Author=Author, zagolovok=zagolovok, comment=comment, date=date)
        if form.is_valid():
        #product.save()
        form.save()
        return super().get(request, *args, **kwargs)

class PostCreateView(CreateView):
    template_name = 'news/news_create.html'
    form_class = PostForm
class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'
    contex_object_name = 'author'

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    #queryset = Products.objects.order_by('-id')
    def get(self, request):
        Posts = Post.objects.order_by('Date')
        p = Paginator(Posts, 10)
        Posts = p.get_page(request.GET.get('page', 10)

        data = {
            'Posts': Posts,
        }
        return render(request, 'news/templates/news.html', data)


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    contex_object_name = 'post'

class CommentList(ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = 'comments'
    paginate_by = 10
    #queryset = Products.objects.order_by('-id')

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    contex_object_name = 'comment'

    def get(self, request):
        Zagolovoks = zagolovok.objects.order_by('name')
        p = Paginator(Zagolovoks, 10)
        Zagolovoks = p.get_page(request.GET.get('page', 10)

        data = {
            'Zagolovoks': Zagolovoks,
        }
        return render(request, 'news/templates/news.html', data)