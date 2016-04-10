from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=500)
  summary = models.CharField(max_length=1000)
  article_text = models.TextField(null=True)
  tags = models.ManyToManyField('Tag', blank=True)
  date_posted = models.DateField(auto_now=False, auto_now_add=True)
  latitude = models.FloatField(default=48.4692338)
  longitude = models.FloatField(default=-123.3698813)

  def __str__(self): 
    return self.title

  class Meta:
    ordering = ['-date_posted']

class Comment(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=254)
  comment_text = models.TextField(null=True)
  article = models.ForeignKey('Article', null=True, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(auto_now_add=True)

  def __str__(self): 
    return self.comment_text

  class Meta:
    ordering = ['date_posted', 'article']

class Tag(models.Model):
  tag_text = models.CharField(max_length=100)

  def __str__(self): 
    return self.tag_text

  class Meta: 
    ordering = ['tag_text']

class Image(models.Model):
  filepath = models.ImageField(max_length=100)
  description = models.CharField(max_length=1000)
  article = models.ForeignKey('Article', on_delete=models.CASCADE)

  def __str__(self): 
    return self.description
