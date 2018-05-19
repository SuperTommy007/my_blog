from ..models import BlogPost
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return BlogPost.objects.all().order_by('-timestamp')[:num]

@register.simple_tag
def archives():
    return BlogPost.objects.dates('timestamp', 'month', order='DESC')