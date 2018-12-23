from django.views import generic
from .models import Competition

class IndexView(generic.ListView):
    template_name = 'competitions/index.html'

    def get_queryset(self):
        return Competition.objects.all()

