from .models import Article, Comment, Tag, Image
from django.contrib import admin

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Image)