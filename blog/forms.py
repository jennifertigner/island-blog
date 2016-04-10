from django import forms
from django.forms import ModelForm
from .models import Comment, Article

class CommentForm(ModelForm): 
  name = forms.CharField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Name'}), 
    label=''
  )
  email = forms.EmailField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), 
    label=''
  )
  comment_text = forms.CharField(
    required=True, 
    widget=forms.Textarea(attrs={'placeholder': 'Your Message'}), 
    label=''
  )
  article = forms.ModelChoiceField(
    queryset=Article.objects.all(), 
    required=False
  )

  class Meta: 
    model = Comment
    fields = ['name', 'email', 'comment_text', 'article']
    exclude = ['date_posted']

class ContactForm(forms.Form):
  contact_name = forms.CharField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Name'}), 
    label=''
    )
  contact_email = forms.EmailField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Email Address'}), 
    label=''
    )
  content = forms.CharField(
    required=True, 
    widget=forms.Textarea(attrs={'placeholder': 'Your Message'}), 
    label=''
    )

class SubscribeForm(forms.Form):
  subscribe_email = forms.EmailField(
    required=True, 
    widget=forms.TextInput(attrs={'placeholder': 'Email address'}), 
    label=''
  )
