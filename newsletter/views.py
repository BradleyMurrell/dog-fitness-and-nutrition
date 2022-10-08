""" Imports """
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers


def subscribe(request):
    """ View for subscribe """
    if request.method == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/subscribe.html', context)


def mail_letter(request):
    """ View for mail letter """
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail_letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mail_letter.html', context)
