from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, AuthorList, AuthorDetail, PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
      # path('', AuthorList.as_view()),
     #  path('<int:pk>', AuthorDetail.as_view()),

       path('', PostList.as_view()),
       path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
       path('create/', PostCreateView.as_view(), name='post_create'),
     #  path('<int:pk>', PostDetail.as_view()),

      # path('', CommentList.as_view()),
      # path('<int:pk>', CommentDetail.as_view()),
]