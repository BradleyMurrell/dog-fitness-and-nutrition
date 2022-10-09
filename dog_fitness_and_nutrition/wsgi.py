"""
WSGI config for dog_fitness_and_nutrition project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'dog_fitness_and_nutrition.settings'
)

application = get_wsgi_application()
