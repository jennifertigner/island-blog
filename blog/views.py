from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from .models import Article, Comment, Tag, Image

def about(request):
  return render(request, 'about/about.html')

def article(request, article_id):
  article = Article.objects.get(pk=article_id)
  image = Image.objects.get(article=article_id)
  # comments = Comment.objects.get(article=article_id)
  return render(request, 'article/article.html', {
    'article': article,  
    'image': image
    # 'comments': comments
  })

def browse(request, tag_word):
  tag = Tag.objects.get(tag_text=tag_word)
  article_list = tag.article_set.all()
  return render(request, 'browse/browse.html', {
    'tag': tag,
    'article_list': article_list
  })

def browse_tag_list(request): 
  tags = Tag.objects.all()
  return render(request, 'browse/tag_list.html', {
    'tags': tags
  })

# WHAT IS THE PROBLEM HERE??? IT RETURNS 3 WHICH GIVES THE ERROR 'RETURNED MORE THAN ONE COMMENT'
# IS THIS ERROR GOING TO REPLICATE FOR IMAGES?
# WHY IS THERE NO ERROR FOR TAGS
def comment(request, article_id=1): 
  article = Article.objects.get(pk=article_id)
  comments = article.comment_set.objects.all()

  # comment_list = ["stuff"]
  # for remark in comment:
  #   comment_list.append(remark)
  return render(request, 'comment/comment.html', {
    'comments': comments,
    # 'comment_list': comment_list
  })

def contact(request):
  return render(request, 'contact/contact.html')

def index(request):
  return render(request, 'main/index.html')

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
