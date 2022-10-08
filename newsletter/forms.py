""" Imports """
from django import forms
from . models import Subscribers, MailMessage


class SubscibersForm(forms.ModelForm):
    """ Model form for subscribers """
    class Meta:
        """ Meta """
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    """ Model form for messages """
    class Meta:
        """ Meta """
        model = MailMessage
        fields = '__all__'
