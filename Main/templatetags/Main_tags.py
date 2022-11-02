import uuid
from django import template

register = template.Library()


@register.simple_tag(name="cache_bust")
def cache_bust():

    version = uuid.uuid1()

    return "v={version}".format(version=version)
