from rest_framework import serializers
from blogsite.blog.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'id_user', 'image', 'date', 'time', 'likes']