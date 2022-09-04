from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import SessionForm

def fitness_plans(request):
    """A view to return the fitness plans page"""

    return render(request, 'fitness_plans/fitness_plans.html')

def fitness_plan_contact(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)

        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            dogs_name = form.cleaned_data['dogs_name']
            dogs_age = form.cleaned_data['dogs_age']
            dogs_breed = form.cleaned_data['dogs_breed']
            sessions = form.cleaned_data['sessions']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('fitness_plans/email/fitness_email.html', {
                'your_name': your_name,
                'dogs_name': dogs_name,
                'dogs_age': dogs_age,
                'dogs_breed': dogs_breed,
                'sessions': sessions,
                'email': email,
                'message': message
            })

            send_mail('Form subject', 'Form message', 'DEFAULT_FROM_EMAIL', ['dog.fitness.nutrition@gmail.com'], html_message=html)

            return render(request, 'contact/contact_success.html')

    form = SessionForm()
    context = {'form': form}
    return render(request, 'fitness_plans/fitness_plan_contact.html', context)
