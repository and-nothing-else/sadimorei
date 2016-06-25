from django.views.generic import ListView, DetailView
from .models import PressRelease


class PressListView(ListView):
    model = PressRelease
    context_object_name = 'articles'
    template_name = 'press/press_list.html'


class PressDetailView(DetailView):
    model = PressRelease
    context_object_name = 'article'
    template_name = 'press/press_detail.html'
