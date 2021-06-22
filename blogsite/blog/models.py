from django.db import models


class AuthUser(models.Model):
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    birthday = models.DateField()
    date_registration = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=50)
    avatar_path = models.ImageField(upload_to='blog-site/blogsite/media')
    id_auth = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(max_length=50)
    enabled = models.BooleanField()

    def __str__(self):
        return self.name


class RoleUser(models.Model):
    class Meta:
        unique_together = (('id_role', 'id_user'),)
    id_role = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()

    def __str__(self):
        return self.id_role


class Comment(models.Model):
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class CommentPost(models.Model):
    class Meta:
        unique_together = (('id_comment', 'id_post'),)
    id_comment = models.IntegerField(primary_key=True)
    id_post = models.IntegerField()

    def __str__(self):
        return self.id_comment


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
    id_category = models.IntegerField(primary_key=True)
    id_post = models.IntegerField()

    def __str__(self):
        return self.id_category


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagPost(models.Model):
    class Meta:
        unique_together = (('id_tag', 'id_post'),)
    id_tag = models.IntegerField(primary_key=True)
    id_post = models.IntegerField()

    def __str__(self):
        return self.id_tag
