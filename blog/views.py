from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext
from .models import Article, Comment, Tag, Image
# for the forms:
from .forms import ContactForm, CommentForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

def about(request):
  tags = Tag.objects.all()
  return render(request, 'about/about.html', {
    'tags': tags
  })

def article(request, article_id):
  tags = Tag.objects.all()
  try:
    article = Article.objects.get(pk=article_id)
  except Article.DoesNotExist:
    return render_to_response('error/404.html')
  image = Image.objects.get(article=article_id)
  comments = Comment.objects.filter(article=article_id).order_by('-date_posted')
  comment_form_class = CommentForm
  if request.method == "POST":
    comment_form = comment_form_class(data=request.POST)
    if comment_form.is_valid():
      new_comment = comment_form.save(commit=False)
      new_comment.article = article
      new_comment.save()
      messages.add_message(request, messages.INFO, 'Your comment has been added')
  return render(request, 'article/article.html', {
    'tags': tags,
    'article': article,  
    'image': image,
    'comments': comments, 
    'comment_form': comment_form_class, 
  })

def browse(request, tag_word):
  tags = Tag.objects.all()
  try:
    tag = Tag.objects.get(tag_text=tag_word)
  except Tag.DoesNotExist:
    return render_to_response('error/404.html')
  article_list = tag.article_set.all()
  all_images = Image.objects.all()
  return render(request, 'browse/browse.html', {
    'tags': tags,
    'tag': tag,
    'article_list': article_list, 
    'all_images': all_images
  })

def contact(request):
  tags = Tag.objects.all()
  form_class = ContactForm
  if request.method == 'POST':
    form = form_class(data=request.POST)
    # checks if info is valid
    if form.is_valid():
      # puts email template together
      contact_name = request.POST.get('contact_name', '')
      contact_email = request.POST.get('contact_email', '')
      form_content = request.POST.get('content', '')
      template = get_template('contact/contact_email_template.txt')
      context = {
        'contact_name': contact_name,
        'contact_email': contact_email,
        'form_content': form_content,
      }
      content = template.render(context)
      # Email the profile with the contact information
      email = EmailMessage(
        "New contact form submission",
        content,
        "Jenn's Little Island Blog" +'',
        ['jennifertigner@gmail.com'],
        headers = {'Reply-To': contact_email }
      )
      email.send()
      messages.add_message(request, messages.INFO, 'Thanks for the message!')
      return redirect('contact')
  return render(request, 'contact/contact.html', {
    'tags': tags,
    'form': form_class
  })

def index(request):
  tags = Tag.objects.all()
  all_articles = get_list_or_404(Article)
  all_comments = Comment.objects.all()
  all_images = Image.objects.all()
  return render(request, 'main/index.html', {
    'tags': tags,
    'all_articles': all_articles,
    'all_comments': all_comments, 
    'all_images': all_images
  })

def search(request):
    tags = Tag.objects.all()
    query = request.GET.get('q')
    all_articles = get_list_or_404(Article)
    all_comments = Comment.objects.all()
    all_images = Image.objects.all()
    return render(request, 'search/search_results.html', {
      'tags': tags,
      'query': query, 
      'all_articles': all_articles,
      'all_comments': all_comments, 
      'all_images': all_images
    })

# ERRORS:

def handler404(request):
  response = render_to_response('error/404.html', {}, 
  context_instance=RequestContext(request))
  response.status_code = 404
  return response

def handler500(request):
  response = render_to_response('error/500.html', {}, 
  context_instance=RequestContext(request))
  response.status_code = 500
  return response
