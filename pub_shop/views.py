from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .paginations import ProductPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'price')

    @action(detail=False)
    def short_list(self, request):
        if 'category' in request.query_params:
            category = request.query_params['category']
            products = Product.objects.filter(category_id=category).select_related('category')[:4]
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response(list())


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
        return get_object_or_404(Product.objects.select_related('category'), slug__iexact=self.kwargs['product_slug'])

class CartPage(TemplateView):
    template_name = 'pages/cart.html'
