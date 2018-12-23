from django.views import generic
from .models import Recent

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    def get_queryset(self):
        return Recent.objects.all()
