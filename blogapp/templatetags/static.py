from django import template
from django.templatetags.static import StaticNode
from random import *
register = template.Library()

class CustomStaticNode(StaticNode):
    def url(self, context):
        version = 2021_10_09
        path = f'{super().url(context)}?v={version}'
        return path


@register.tag('static')
def do_static(parser, token):
    node = CustomStaticNode.handle_token(parser, token)
    return node