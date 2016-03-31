from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from .models import Article, Comment, Tag, Image

def index(request):
  return render(request, 'main/index.html')

def browse_tag_list(request): 
  list = []
  tags = Tag.objects.all()
  for tag in tags:
    word = tag.tag_text
    list.append(word)
  return render(request, 'browse/tag_list.html', {
    'list': list
  });

def browse(request, tag_word):
  word = Tag.objects.get(tag_text=tag_word)
  article_list = word.article_set.all()
  return render(request, 'browse/browse.html', {
    'word': word, 
    'article_list': article_list
  });

def about(request):
  return render(request, 'about/about.html')

def contact(request):
  return render(request, 'contact/contact.html')

def article(request, article_id):
  article = Article.objects.get(pk=article_id)
  title = article.title
  summary = article.summary
  article_text = article.article_text
  tags = article.tags.all()
  date_posted = article.date_posted
  comment_count = article.comment_count
  image = Image.objects.get(article=article)
  image_description = image.description
  return render(request, 'article/article.html', {
    'article': article, 
    'title': title, 
    'summary': summary, 
    'article_text': article_text, 
    'tags': tags, 
    'date_posted': date_posted, 
    'comment_count': comment_count, 
    'image': image,
    'image_description': image_description
  });

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
