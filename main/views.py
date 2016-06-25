from django.views.generic import TemplateView


class ParentTemplateMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_template'] = 'ajax.html' if self.request.is_ajax() else 'base.html'
        return context


class HomeView(TemplateView):
    template_name = 'main/home.html'
