from django.urls import path
from .views import AuthorList, AuthorDetail, PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
       path('', AuthorList.as_view()),
       path('<int:pk>', AuthorDetail.as_view()),

       path('', PostList.as_view()),
       path('<int:pk>', PostDetail.as_view()),

       path('', CommentList.as_view()),
       path('<int:pk>', CommentDetail.as_view()),
]