from django import template
from markdown_it import MarkdownIt

register = template.Library()


@register.filter
def markdownit(text: str):
    md = MarkdownIt()
    return md.render(text)
