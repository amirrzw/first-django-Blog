from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articlesList.html', args)


def article_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, 'article_details.html', {'article': article})
