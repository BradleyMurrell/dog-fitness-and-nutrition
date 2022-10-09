""" Imports """
from django import forms


class ContactForm(forms.Form):
    """ Form model for contact form """
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
