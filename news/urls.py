from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'news'
urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]