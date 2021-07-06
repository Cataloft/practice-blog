from django.shortcuts import render, redirect, get_object_or_404
from operator import attrgetter
from blog.models import *
from account.models import Account
from blog.forms import CreatePostForm, UpdatePostForm
from django.http import HttpResponse


def home_view(request):
    context = {}

    posts = sorted(Post.objects.all(), key=attrgetter('date_updated'), reverse=True)
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


def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreatePostForm(request.POST or None, request.FILES or None)
    if form.is_valid:
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreatePostForm()

    context['form'] = form

    return render(request, 'blog/create_blog.html', context)


def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(Post, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(Post, slug=slug)

    if blog_post.author != user:
        return HttpResponse('you are not the author of that post')

    if request.POST:
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
    form = UpdatePostForm(
        initial={
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )
    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)
