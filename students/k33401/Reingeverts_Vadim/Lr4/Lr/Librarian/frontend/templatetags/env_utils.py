from django.template.defaulttags import register
import os


@register.simple_tag
def get_env(key, defaultValue=None):
    return os.environ.get(key, defaultValue)
