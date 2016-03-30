from django.shortcuts import render
from django.template import RequestContext
from .models import Article, Comment, Tag, Image

def index(request):
  return render(request, 'homepage/index.html')

def browse_tag_list(request): 
  return render(request, 'browse/tag_list.html')

def browse(request, tag_id):
  return render(request, 'browse/browse.html')

def about(request):
  return render(request, 'about/about.html')

def contact(request):
  return render(request, 'contact/contact.html')

def article(request, article_id):
  return render(request, 'article/article.html')


# def error404(request):
#   response = render_to_response('error/404.html', {},
#   context_instance=RequestContext(request))
#   response.status_code = 404
#   return response

# def error500(request):
#   response = render_to_response('error/500.html', {},
#   context_instance=RequestContext(request))
#   response.status_code = 500
#   return response
