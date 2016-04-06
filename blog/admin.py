from .models import Article, Comment, Tag, Image
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Image)