from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Role)
admin.site.register(RoleUser)
admin.site.register(Comment)
admin.site.register(CommentPost)
admin.site.register(Category)
admin.site.register(CategoryPost)
admin.site.register(Tag)
admin.site.register(TagPost)
admin.site.register(Photo)




