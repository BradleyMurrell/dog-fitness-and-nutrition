""" Imports """
from django.db import models


class Subscribers(models.Model):
    """ Model for subscribing """
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)


class MailMessage(models.Model):
    """ Model for sending messages to subscribers """
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
