# https://wsvincent.com/django-referencing-the-user-model/
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from datetime import datetime
from .models import Book, Author
from django.db import models



@login_required(login_url='/bibliothek/register_user/')
def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    return render(request, 'bibliothek/index.html', {'authors': authors, 'books': books})


def check_book(request):
    book_title = request.POST['Book']
    title = Book(title=book_title)
    title.save()
    return HttpResponseRedirect(reverse('bibliothek:index'))

def add_book(request):
    book_title = request.POST['book']
    author_id = request.POST['author_id']
    pub_date = request.POST['pub_date']
    pub_date = datetime.strptime(pub_date, '%Y-%m-%d')
    title = Book(title=book_title, author_id=author_id, pub_date=pub_date)
    title.save()
    return HttpResponseRedirect(reverse('bibliothek:index'))

def check_author(request):
    author = request.POST['Author']
    author_name = Author(name=author)
    author_name.save()
    return HttpResponseRedirect(reverse('bibliothek:index'))

def checkout(request):
    book_id = request.POST['book_id']
    # book = Book.objects.get(pk=book_id, user_check_out=user_check_out)
    book = Book.objects.get(pk=book_id)
    book.check_out = not book.check_out
    book.save()
    return HttpResponseRedirect(reverse('bibliothek:index'))


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('bibliothek:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('bibliothek:index'))
    return HttpResponseRedirect(reverse('bibliothek:register'))


def register(request):
    return render(request, 'bibliothek/register.html', {})


def logout_user(request):
    logout(request)
    return render(request, 'bibliothek/register.html', {})