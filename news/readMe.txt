from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment


def init():

    print(f'DB initialization started...')

    print(f' Очистка объектов...')
    PostCategory.objects.all().delete()
    print(f'  PostCategories = {PostCategory.objects.count()}')
    Category.objects.all().delete()
    print(f'  Categories = {Category.objects.count()}')
    Author.objects.all().delete()
    print(f'  Authors = {Author.objects.count()}')
    User.objects.all().delete()
    print(f'  Users = {User.objects.count()}')
    print(f' Очистка объектов завершена')

    print(f' Ввод новых данных...')
    print(f'  Создание пользователей и авторов...')
    User(username="user1").save()
    User(username="user2").save()
    User(username="comment_user1").save()
    User(username="comment_user2").save()
    print(f'   Users = {User.objects.count()}')

    Author(user=User.objects.get(username="user1"), author_name="author1").save()
    Author(user=User.objects.get(username="user2"), author_name="author2").save()
    print(f'   Authors = {Author.objects.count()}')
    print(f'  Пользователи и авторы созданы')

    print(f'  Создание категорий...')
    c1 = Category(name="cat1")
    c1.save()
    c2 = Category(name="cat2")
    c2.save()
    c3 = Category(name="cat3")
    c3.save()
    c4 = Category(name="cat4")
    c4.save()
    print(f'   Categories = {Category.objects.count()}')
    print(f'  Категории созданы')

    print(f'  Создание постов...')
    print(f'   Пост 1...')
    a = Author.objects.get(author_name='author1')
    p = Post(post_type='0', author=a, post_header='PostHeader1', post_body='post_body1', rating=1)
    p.save()
    print(f'   Пост 1 создан')
    print(f'   Пост 1. Присвоение категорий...')
    PostCategory(post=p, category=c1).save()
    PostCategory(post=p, category=c2).save()
    print(f'   Пост 1. Категории присвоены')
    print(f'   Пост 2...')
    p = Post(post_type='1', author=a, post_header='PostHeader2', post_body='post_body2', rating=4)
    p.save()
    print(f'   Пост 2 создан')
    print(f'   Пост 2. Присвоение категории...')
    PostCategory(post=p, category=c3).save()
    print(f'   Пост 2. Категория присвоена')
    print(f'   Пост 3...')
    a = Author.objects.get(author_name='author2')
    p = Post(post_type='1', author=a, post_header='NewsHeader3', post_body='news_body1', rating=5)
    p.save()
    PostCategory(post=p, category=c4).save()
    print(f'   Пост 3 создан')
    print(f'   Posts = {Post.objects.count()}')
    print(f'  Посты созданы')
    print(f' Ввод новых данных завершён')

    print(f'  Создание комментов...')
    p1 = Post.objects.get(post_header='PostHeader1')
    p2 = Post.objects.get(post_header='PostHeader2')
    u1 = User.objects.get(username='comment_user1')
    Comment(post=p1, user=u1, comment_text='Комментарий №1. Текст комментария', rating=1).save()
    u2 = User.objects.get(username='comment_user2')
    Comment(post=p1, user=u2, comment_text='Комментарий №2. Грамотно излагаешь! Уважаю!', rating=2).save()

    Comment(post=p2, user=u1, comment_text='Комментарий №3. Текст комментария', rating=1).save()
    p2 = Post.objects.get(post_header='NewsHeader3')
    Comment(post=p2, user=u1, comment_text='Комментарий №4. 1 Комментарий к новости', rating=1).save()
    Comment(post=p2, user=u2, comment_text='Комментарий №5. 2 Комментарий к новости', rating=2).save()

    print(f'   Comments = {Comment.objects.count()}')
    print(f'  Комментарии созданы')

    print(f'DB initialization complete')


def acts():
    # >>> from db_actions import acts
    # >>> acts()

    init()

    # 1. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
    print('1. Ставим лайки и дизлайки...')
    p1 = Post.objects.get(post_header='PostHeader1')
    p1.like()
    p1.dislike()
    p1.dislike()

    # 2. Обновить рейтинги пользователей.
    print('2. Рейтинги пользователей')
    print(' Обновление рейтингов пользователей...')
    for a in Author.objects.all():
        a.update_rating()
    # print(Author.objects.all().values('author_name', 'rating'))
    print(' Обновление рейтингов пользователей завершено')

    # 3. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
    a = Author.objects.all().order_by('-rating')[:1][0]
    print(f"3. Лучший пользователь (по версии Forbes):")
    print(f' Имя: {a.user.username}')
    print(f' Рейтинг: {a.rating}')

    # 4. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на
    #    лайках/дислайках к этой статье.
    # лучший пост - аналог SELECT TOP 1 ... ORDER BY rating DESC
    print('4. Лучшая статья:')
    p = Post.objects.all().order_by('-rating')[:1][0]
    print(f' Дата добавления статьи: {p.input_date_time.strftime("%d.%m.%Y %H:%M:%S")}')
    print(f' Автор: {p.author.author_name}')
    print(f' Рейтинг автора: {p.author.rating}')
    print(f' Заголовок статьи: "{p.post_header}"')
    print(f' Preview статьи: "{p.preview()}"')

    # 5. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
    cs = Comment.objects.filter(post=p)
    print(f'5. Комментарии к статье: {cs.count()}')
    n = 1
    for c in cs:
        print(f' Комментарий №{n}')
        print(f'  Дата комментария: {c.input_date_time.strftime("%d.%m.%Y %H:%M:%S")}')
        print(f'  Пользователь: {c.user.username}')
        print(f'  Рейтинг комментария: {c.rating}')
        print(f'  Текст комментария: {c.comment_text}')
        n += 1