from django.urls import path

from blog.api.view import api_detail_post_view

app_name = 'blog'

url_patterns = [
    path('<slug>/', api_detail_post_view, name="detail"),
]