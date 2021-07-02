from django.db import models
from account.models import Account
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(max_length=50)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RoleUser(models.Model):
    class Meta:
        unique_together = (('id_role', 'id_user'),)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    id_user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class CommentPost(models.Model):
    class Meta:
        unique_together = (('id_comment', 'id_post'),)
    id_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Photo(models.Model):
    path = models.ImageField(upload_to='blog-site/blogsite/media')
    description = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.path


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CategoryPost(models.Model):
    class Meta:
        unique_together = (('id_category', 'id_post'),)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagPost(models.Model):
    class Meta:
        unique_together = (('id_tag', 'id_post'),)
    id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)

