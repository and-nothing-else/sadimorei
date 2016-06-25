import os
from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import ExtendFlatpage


def get_flatpages_templates():
    template_list = os.listdir(os.path.join(settings.BASE_DIR, 'extendflatpages/templates/flatpages'))

    templates = [(os.path.join('flatpages', template), template) for template in template_list]

    return templates


class ExtendFlatPageForm(FlatpageForm):

    class Meta:
        model = ExtendFlatpage
        fields = '__all__'

        widgets = {
            'content': CKEditorUploadingWidget(),
            'template_name': forms.Select(choices=get_flatpages_templates()),
        }

    def __init__(self, *args, **kwargs):
        super(ExtendFlatPageForm, self).__init__(*args, **kwargs)
        self.fields['sites'].initial = [settings.SITE_ID]


class ExtendFlatPageAdmin(FlatPageAdmin):
    form = ExtendFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced options'), {'fields': ('template_name', 'sites',)})
    )
    list_filter = ()


admin.site.unregister(FlatPage)
admin.site.register(ExtendFlatpage, ExtendFlatPageAdmin)
