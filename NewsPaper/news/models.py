from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum

# длина начала текста поста для предпросмотра
PREVIEW_LEN = 124

class Author(models.Model):
    author_name = models.CharField(max_length=255)
    reit = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self): #суммарный рейтинг каждой статьи автора умножается на 3;
                            #суммарный рейтинг всех комментариев автора;
                            #суммарный рейтинг всех комментариев к статьям автора.
        n1 = Post.objects.filter(author=self.id).aggregate(rating=Sum('reit'))['reit'] * 3

        cr = Comment.objects.filter(user=self.user).aggregate(comments_rating=Sum('reit_Commit'))
        if not cr['reit_Commit'] is None:
            n1 += cr['reit_Commit']

        for i in Post.objects.filter(author=self.id, post_type='0'):
            n1 += Comment.objects.filter(post=i).aggregate(post_rating=Sum('reit'))['reit_Commit']

        self.reit = n1
        self.save()
        return n1

class Category(models.Model):
    TEMAS = [
        (sport, 'спорт'),
        (politik, 'политика'),
        (knowlength, 'образование'),
        (biznes, 'бизнес'),
        (other, 'разное'),
    ]
    TEMA = models.CharField(max_length=255, choices=TEMAS, default=other, unique=True)

POST_TYPE = [('0', 'статья'), ('1', 'новость')]

class Post(models.Model):
    post_type = models.CharField(max_length=1, choices=POST_TYPE, default='0')
    time_in = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    zagolovok = models.CharField(max_length=255)
    novosti = models.TextField(default="Новость в разработке")
    reit_Novosti = model.IntegerField(default=0)
    #Post = models.ManyToManyField(Author, through='ProductOrder')

    def like(self):
        self.reit_Novosti += 1

    def dislike(self):
        self.reit_Novosti -= 1
     #возвращает начало статьи (предварительный
                        # просмотр) длиной 124 символа и
                         # добавляет многоточие в конце.
def preview(self):
    if len(self.novosti) > PREVIEW_LEN:
        return self.novosti[:PREVIEW_LEN + 1] + '...'
    else:
        return self.novosti

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    komment = models.TextField(default="без комментариев")
    time_Commit = models.DateTimeField(auto_now_add=True)
    reit_Commit = model.IntegerField(default=0)

    def like(self):
        self.reit_Commit += 1

    def dislike(self):
        self.reit_Commit -= 1


