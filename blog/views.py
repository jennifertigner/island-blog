from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from .models import Article, Comment, Tag, Image

def about(request):
  return render(request, 'about/about.html')

def article(request, article_id):
  article = Article.objects.get(pk=article_id)
  image = Image.objects.get(article=article_id)
  comments = Comment.objects.filter(article=article_id).order_by('-date_posted')
  return render(request, 'article/article.html', {
    'article': article,  
    'image': image,
    'comments': comments
  })

def browse(request, tag_word):
  tag = Tag.objects.get(tag_text=tag_word)
  article_list = tag.article_set.all()
  return render(request, 'browse/browse.html', {
    'tag': tag,
    'article_list': article_list
  })

def contact(request):
  return render(request, 'contact/contact.html')

def index(request):
  all_articles = Article.objects.all()
  all_comments = Comment.objects.all()
  all_images = Image.objects.all()
  return render(request, 'main/index.html', {
    'all_articles': all_articles,
    'all_comments': all_comments, 
    'all_images': all_images
  })

def error404(request):
  response = render('error/404.html', {},
  context_instance=RequestContext(request))
  response.status_code = 404
  return response

def error500(request):
  response = render('error/500.html', {},
  context_instance=RequestContext(request))
  response.status_code = 500
  return response
