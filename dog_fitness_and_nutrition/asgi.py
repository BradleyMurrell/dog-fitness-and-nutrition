"""
ASGI config for dog_fitness_and_nutrition project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'dog_fitness_and_nutrition.settings'
)

application = get_asgi_application()
