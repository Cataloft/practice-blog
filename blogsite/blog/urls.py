from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'


urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_blog_view, name='create'),
    path('<slug>/', detail_blog_view, name='detail'),
    path('<slug>/edit', edit_blog_view, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)