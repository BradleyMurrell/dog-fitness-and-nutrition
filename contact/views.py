""" Imports """
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    """ View for contact """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contact/email/email.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail(
                'Form subject',
                'Form message',
                'DEFAULT_FROM_EMAIL',
                ['dog.fitness.nutrition@gmail.com'],
                html_message=html
            )

            return render(request, 'contact/contact_success.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
