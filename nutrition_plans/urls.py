""" Imports """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition_plans, name='nutrition_plans'),
    path(
        'nutrition_plan_contact',
        views.nutrition_plan_contact,
        name='nutrition_plan_contact'
    )
]
