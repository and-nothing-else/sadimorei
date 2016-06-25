from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy
from .forms import FeedbackForm
from main.views import ParentTemplateMixin


class FeedbackFormView(ParentTemplateMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/form.html'
    success_url = reverse_lazy('feedback:thanks')


class FeedbackSuccessView(ParentTemplateMixin, TemplateView):
    template_name = 'feedback/thanks.html'
