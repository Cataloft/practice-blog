from rest_framework import serializers
from blog.models import *
from account.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'image', 'date', 'time', 'likes']