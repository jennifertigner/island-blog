from .forms import SubscribeForm
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

def subscribe_form(request):
  subscribe_form = SubscribeForm
  if request.method == 'POST':
    form = subscribe_form(data=request.POST)
    if form.is_valid():
      subscribe_email = request.POST.get('subscribe_email', '')
      context = {'subscribe_email': subscribe_email}

      # email to me when a new user subscribes
      template_new_user = get_template('main/subscription_request_template.txt')
      content_new_user = template_new_user.render(context)
      email_to_me = EmailMessage(
        "New subscription request",
        content_new_user,
        "Jenn's Little Island Blog" +'',
        ['jennifertigner@gmail.com']
      )
      email_to_me.send()

      # email to the user as a welcome
      template_welcome_email = get_template('main/welcome_email_template.txt')
      content_welcome_email = template_welcome_email.render(context)
      email_to_subscriber = EmailMessage(
        "Welcome to the Island",
        content_welcome_email,
        "Jenn's Little Island Blog" +'',
        [subscribe_email]
      )
      email_to_subscriber.send()
      message = messages.add_message(request, messages.SUCCESS, 'Thanks for subscribing!')
  return {
   'subscribe_form': SubscribeForm()
  }
