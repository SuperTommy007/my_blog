from ..models import BlogPost,Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return BlogPost.objects.all().order_by('-timestamp')[:num]

@register.simple_tag
def archives():
    return BlogPost.objects.dates('timestamp', 'month', order='DESC')

@register.simple_tag
def categorys():
    return Category.objects.all()