from .models import Page
from django.views.generic import DetailView, TemplateView


class HomePage(TemplateView):
    template_name = 'pages/home.html'


class PageDetail(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
