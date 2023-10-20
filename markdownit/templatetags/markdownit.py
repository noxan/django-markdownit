from django import template
from django.utils.safestring import mark_safe
from markdown_it import MarkdownIt

register = template.Library()


@register.filter
def markdownit(text: str):
    md = MarkdownIt()
    html = md.render(text)
    return mark_safe(html)
