from django.views.generic import ListView
from contact.models import Office


class MapView(ListView):
    model = Office
    template_name = 'contact/map_view.html'
    context_object_name = 'office_list'
