from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='censor')
def censor(value):
    unwanted_words = ['нежелательное_слово1', 'нежелательное_слово2', ...]
    censored_value = value

    for word in unwanted_words:
        censored_value = censored_value.replace(word, '*' * len(word))

    return mark_safe(censored_value)