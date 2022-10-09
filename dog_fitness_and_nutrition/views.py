""" Imports """
from django.shortcuts import render


def handler404(request, *args, **argv):
    """ View for 404 error """
    return render(request, 'errors/404.html')
