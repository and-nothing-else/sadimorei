from django.views.generic import ListView
from .models import Publication


class PublicationListView(ListView):
    model = Publication
    context_object_name = 'publications'
    template_name = 'publications/publication_list.html'
