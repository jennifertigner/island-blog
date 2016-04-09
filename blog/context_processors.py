from .forms import SubscribeForm
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

def subscribe_form(request):
  subscribe_form = SubscribeForm
  if request.method == 'POST':
    form = subscribe_form(data=request.POST)
    contact_email = request.POST.get('contact_email', '')
    context = {'contact_email': contact_email}

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
      [contact_email]
    )
    email_to_subscriber.send()
    messages.add_message(request, messages.INFO, 'Thanks for subscribing!')
  return {
   'subscribe_form': SubscribeForm()
  }
