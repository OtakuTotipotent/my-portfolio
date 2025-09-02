from django import template

register = template.Library()


@register.filter(name="markdown")
def markdown_format(text):
    return text.replace("**", "<strong>").replace("**", "</strong>")
