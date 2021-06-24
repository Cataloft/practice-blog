from django.shortcuts import render
from .models import *


def home_view(request):
    context = {}
    posts = Post.objects.all()
    context['post'] = posts
    return render(request, 'blog/home.html', context)
