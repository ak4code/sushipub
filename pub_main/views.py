from .models import Page
from django.views.generic import DetailView, TemplateView
from pub_shop.models import Category


class HomePage(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('products').exclude(products__isnull=True)
        return context


class OrderView(TemplateView):
    template_name = 'pages/orders.html'


class PageDetail(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
