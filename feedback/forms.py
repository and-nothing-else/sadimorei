from django import forms
from .models import Feedback
from django.utils.translation import ugettext_lazy as _


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label=_('Your name'), max_length=256,
                           widget=forms.TextInput(attrs={'class': 'span6', 'required': 'required'}))
    contact = forms.CharField(label=_('Your phone or email'), max_length=512,
                              widget=forms.TextInput(attrs={'class': 'span6', 'required': 'required'}))
    message = forms.CharField(label=_('Your message'),
                              widget=forms.Textarea(attrs={'class': 'span6', 'required': 'required'}))

    class Meta:
        model = Feedback
        fields = [
            'name',
            'contact',
            'message',
        ]
