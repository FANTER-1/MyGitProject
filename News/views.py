from django.shortcuts import render
from .models import News
from django.template.defaulttags import register

@register.filter
def censor(value):
    bad_words = ['нежелательное_слово1', 'нежелательное_слово2']  # список нежелательных слов
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value

def news_list(request):
    news = News.objects.order_by('-publish_date')  # отсортировать новости по дате публикации
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})