from django.shortcuts import render_to_response
from .models import Doc, Certificate


def doc_list(request):
    return render_to_response('docs/doc_list.html', {
        'docs': Doc.objects.all(),
        'certificates': Certificate.objects.all()
    })
