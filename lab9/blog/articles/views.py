# Create your views here.
# -*- coding: utf-8 -*-
from models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous():
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                for a in Article.objects.all():
                    if form["title"] == a.title:
                        form['errors'] = u"Статья с таким названием уже существует!"
                        return render(request, 'create_post.html', {'form': form})
                # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"],
                    title=form["title"],
                    author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def registrate(request):
    if not request.user.is_anonymous():
        return redirect('archive')
    if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'username': request.POST["username"],
                'email': request.POST["email"],
                'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["email"] and form["password"]:
                try:
                    User.objects.get(username=form["username"])
                    form['errors'] = u"Такой юзер уже существует"
                    return render(request, 'registration.html', {'form': form})
                except:
                     # если поля заполнены без ошибок
                    User.objects.create_user(form["username"], form["email"], form["password"])
               
                    # перейти на главную 
                    return redirect('archive')
            
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'registration.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        
        return render(request, 'registration.html', {})


def loginView(request):
    if not request.user.is_anonymous():
        return redirect('archive')
    if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'username': request.POST["username"],
                'email': request.POST["email"],
                'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["username"] and form["email"] and form["password"]:
                user = authenticate(username=form["username"], password=form["password"])
                if user == None:
                    form['errors'] = u"Такого пользователя нет"
                    return render(request, 'login.html', {'form': form})
                else:
                    login(request, user)
                    return redirect('archive')
            
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'login.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'login.html', {})
