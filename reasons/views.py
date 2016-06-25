from django.views.generic import ListView
from .models import Reason


class ReasonListView(ListView):
    model = Reason
    template_name = 'reasons/reason_list.html'
    context_object_name = 'reasons'
