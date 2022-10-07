""" Imports """
from django import forms


class SessionForm(forms.Form):
    """ Form model for fitness plan """

    SESSION = (
        ('try', 'Try'),
        ('term', 'Term'),
        ('single session', 'Single session'),
    )

    your_name = forms.CharField(max_length=255)
    dogs_name = forms.CharField(max_length=255)
    dogs_age = forms.CharField(max_length=255)
    dogs_breed = forms.CharField(max_length=255)
    sessions = forms.ChoiceField(choices=SESSION)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
