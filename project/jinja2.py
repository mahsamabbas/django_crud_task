from jinja2 import Environment
from django.urls import reverse


def environment(**options):
    env = Environment(**options)
    env.autoescape = True
    env.globals.update({'url': reverse})
    return env
