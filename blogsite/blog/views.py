from django.shortcuts import render, redirect
from .models import *
from account.models import Account


def home_view(request):
    context = {}

    posts = Post.objects.all()
    tags = TagPost.objects.all()
    categories = CategoryPost.objects.all()
    photos = Photo.objects.all()
    accounts = Account.objects.all()

    context['accounts'] = accounts
    context['posts'] = posts
    context['tags'] = tags
    context['categories'] = categories
    context['photos'] = photos

    return render(request, 'blog/home.html', context)

