from django import forms
from django.forms import ModelForm
from .models import Comment, Article

class CommentForm(ModelForm): 
  article = forms.ModelChoiceField(queryset=Article.objects.all(), required=False)
  class Meta: 
    model = Comment
    fields = ['name', 'email', 'comment_text', 'article']
    exclude = ['date_posted']

class ContactForm(forms.Form):
  contact_name = forms.CharField(required=True)
  contact_email = forms.EmailField(required=True)
  content = forms.CharField(required=True, widget=forms.Textarea)

class SubscribeForm(forms.Form):
  contact_email = forms.EmailField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Email address'}), 
    label=''
  )
