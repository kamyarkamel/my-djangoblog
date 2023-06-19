from django.shortcuts import render
from .models import Article


# Create your views here.
def articles(request):
    articles_name = Article.objects.all().order_by('date')
    args = {'articles': articles_name}
    return render(request, 'articles/articles.html', args)
