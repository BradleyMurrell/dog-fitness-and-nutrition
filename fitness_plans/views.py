from django.shortcuts import render

# Create your views here.

def fitness_plans(request):
    """A view to return the fitness plans page"""

    return render(request, 'fitness_plans/fitness_plans.html')

def fitness_plan_contact(request):
    """A view to return the fitness plan contact page"""

    return render(request, 'fitness_plans/fitness_plan_contact.html')
