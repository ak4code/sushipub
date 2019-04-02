from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'pub_shop/category_detail.html'

    def get_object(self):
        return get_object_or_404(Category, slug__iexact=self.kwargs['slug'])

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pub_shop/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, slug__iexact=self.kwargs['slug'])