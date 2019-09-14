from django.views import generic


# Create your views here.

class RealtimeIndex(generic.TemplateView):
    template_name = "index.html"
