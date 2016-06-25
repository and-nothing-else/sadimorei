from django.views.generic import ListView, DetailView
from .models import News


class NewsListView(ListView):
    queryset = News.actual.all()
    context_object_name = 'articles'
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    queryset = News.actual.all()
    context_object_name = 'article'
    template_name = 'news/news_detail.html'
