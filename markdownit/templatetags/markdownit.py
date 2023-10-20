from django import template
from markdown_it import MarkdownIt

register = template.Library()


@register.filter
def markdown(text: str):
    md = MarkdownIt()
    return md.render(text)
