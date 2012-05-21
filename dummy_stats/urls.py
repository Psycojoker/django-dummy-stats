from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from models import Request

class Home(TemplateView):
    template_name="dummy_stats/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["requests"] = Request
        return context

urlpatterns = patterns('',
    url(r'^$', Home.as_view()),
)
