from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_plans, name='fitness_plans'),
    path('fitness_plan_contact', views.fitness_plan_contact, name='fitness_plan_contact')
]
