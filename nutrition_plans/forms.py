""" Imports """
from django import forms


class SessionForm(forms.Form):
    """ Form model for nutrition plan """

    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    PHYSIQUE = (
        ('thin', 'Thin'),
        ('ideal', 'Ideal weight'),
        ('large', 'Could lose some weight')
    )

    ACTIVITY = (
        ('lazy', 'Lazy couch potato'),
        ('active', 'Active'),
        ('athlete', 'Athletic')
    )

    HABITS = (
        ('very picky', 'Very Picky'),
        ('sometimes picky', 'Sometimes Picky'),
        ('eats anything', 'Eats Anything')
    )

    PREFERENCE = (
        ('grain free', 'Grain free diet'),
        ('grain inclusive', 'Grain inclusive diet'),
        ('either', 'Either, please recommend')
    )

    GOAL = (
        ('digestion', 'Digestion'),
        ('heart health', 'Heart health'),
        ('skin coat', 'Skin/Coat'),
        ('hip joint', 'Hip and joint health'),
        ('longevity', 'Life longevity'),
        ('stress anxiety', 'Stress and anxiety'),
        ('weight loss', 'Weight loss'),
        ('weight gain', 'Weight gain'),
    )

    your_name = forms.CharField(max_length=255)
    dogs_name = forms.CharField(max_length=255)
    dogs_age = forms.CharField(max_length=255)
    dogs_breed = forms.CharField(max_length=255)
    dogs_gender = forms.ChoiceField(choices=GENDER)
    dogs_weight = forms.CharField(max_length=255)
    dogs_physique = forms.ChoiceField(choices=PHYSIQUE)
    active_level = forms.ChoiceField(choices=ACTIVITY)
    eating_habit = forms.ChoiceField(choices=HABITS)
    allergies = forms.CharField(max_length=255)
    food_preference = forms.ChoiceField(choices=PREFERENCE)
    outcome_goal = forms.ChoiceField(choices=GOAL)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
