from django.template.defaulttags import register
import os


@register.filter
def get_env(key):
    return os.environ.get(key, 3000)
