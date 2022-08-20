from django.shortcuts import render

# Create your views here.

def nutrition_plans(request):
    """A view to return the nutrition plans page"""

    return render(request, 'nutrition_plans/nutrition_plans.html')
