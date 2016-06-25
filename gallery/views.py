from django.views.generic import ListView
from .models import Photo


class GalleryListView(ListView):
    model = Photo
    context_object_name = 'photo_list'
    template_name = 'gallery/gallery.html'
