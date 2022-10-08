""" Imports """
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import SubscibersForm, MailMessageForm


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
    form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mail_letter.html', context)
