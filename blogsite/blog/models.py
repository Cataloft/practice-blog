from django.db import models
from account.models import Account

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(null=True, blank=False)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.email + "-" + instance.title)


pre_save.connect(pre_save_post_receiver, sender=Post)


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

