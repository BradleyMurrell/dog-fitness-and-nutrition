""" Imports """
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import SessionForm


def nutrition_plans(request):
    """A view to return the nutrition plans page"""

    return render(request, 'nutrition_plans/nutrition_plans.html')


def nutrition_plan_contact(request):
    """A view to return the nutrition plan contact page"""
    if request.method == 'POST':
        form = SessionForm(request.POST)

        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            dogs_name = form.cleaned_data['dogs_name']
            dogs_age = form.cleaned_data['dogs_age']
            dogs_breed = form.cleaned_data['dogs_breed']
            dogs_gender = form.cleaned_data['dogs_gender']
            dogs_weight = form.cleaned_data['dogs_weight']
            dogs_physique = form.cleaned_data['dogs_physique']
            active_level = form.cleaned_data['active_level']
            eating_habit = form.cleaned_data['eating_habit']
            allergies = form.cleaned_data['allergies']
            food_preference = form.cleaned_data['food_preference']
            outcome_goal = form.cleaned_data['outcome_goal']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string(
                'nutrition_plans/email/nutrition_email.html', {
                    'your_name': your_name,
                    'dogs_name': dogs_name,
                    'dogs_age': dogs_age,
                    'dogs_breed': dogs_breed,
                    'dogs_gender': dogs_gender,
                    'dogs_weight': dogs_weight,
                    'dogs_physique': dogs_physique,
                    'active_level': active_level,
                    'eating_habit': eating_habit,
                    'allergies': allergies,
                    'food_preference': food_preference,
                    'outcome_goal': outcome_goal,
                    'email': email,
                    'message': message
                }
            )

            send_mail(
                'Form subject',
                'Form message',
                'DEFAULT_FROM_EMAIL',
                ['dog.fitness.nutrition@gmail.com'],
                html_message=html
            )

            return render(request, 'contact/contact_success.html')

    form = SessionForm()
    context = {'form': form}
    return render(
        request,
        'nutrition_plans/nutrition_plan_contact.html',
        context
    )
