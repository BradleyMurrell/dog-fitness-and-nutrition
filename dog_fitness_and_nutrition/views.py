from django.shortcuts import render


def handler404(request, *args, **argv):
    return render(request, 'errors/404.html')
