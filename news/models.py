from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum
from django.core.validators import MinValueValidator

# длина начала текста поста для предпросмотра
PREVIEW_LEN = 124

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.IntegerField(default=0,
       validators=[MinValueValidator(0)],)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat +=postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentsRating=Sum('rating'))
        cRat = 0
        cRat +=commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    zagolovok = models.CharField(max_length=255, unique=True)
    novosti = models.TextField(default="Новость в разработке")
    rating = models.IntegerField(default=0,
       validators=[MinValueValidator(0)],)

    ARTICLE = 'AR'
    NEWS = 'NW'

    POST_TYPES = [
        (ARTICLE, 'статья'),
        (NEWS, 'новость'),
    ]
    post_type = models.CharField(max_length=2, choices=POST_TYPES, default=ARTICLE)
    time_in = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f'Post #{self.pk} - Name: {self.zagolovok}'

    def get_absolute_url(self):
        return f'/post/{self.id}'


    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
     #возвращает начало статьи (предварительный
                        # просмотр) длиной 124 символа и
                         # добавляет многоточие в конце.
def preview(self):
    if len(self.novosti) > PREVIEW_LEN:
        return self.novosti[:PREVIEW_LEN + 1] + '...'
    else:
        return self.novosti

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(default="без комментариев")
    date_Commit = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0,
       validators=[MinValueValidator(0)],)

    def __str__(self):
       return self.commentUser.username

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1


