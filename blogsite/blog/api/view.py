from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import *
from blog.models import *
from blog.api.serializers import *

@api_view(['GET', ])
def api_detail_post_view(request, slug):
    try:
        blog_post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(blog_post)
        return Response(serializer.data)
