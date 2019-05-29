from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from vk_api.utils import get_random_id

from pub_shop.permissions import ClientAppPermission
from sushipub.vkbot import vk
from .models import Category, Product, Destination, Order
from .serializers import CategorySerializer, ProductSerializer, DestinationSerializer, OrderSerializer
from .paginations import ProductPagination
from .pusher import socket


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('products')
    serializer_class = CategorySerializer


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items', 'items__product', 'items__product__ingredients',
                                              'items__product__category')
    serializer_class = OrderSerializer

    @action(detail=False, methods=['post'], permission_classes=[ClientAppPermission], name='Checkout')
    def checkout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        instance = serializer.save()
        inputs = ['%s' % (item) for item in instance.items.all()]
        items = '\n'.join(inputs)
        total = instance.total()
        message = f'Новый заказ! \n' \
            f'Имя: {instance.name}\n' \
            f'Телефон: {instance.phone}\n' \
            f'Район доставки: {instance.area.name}\n' \
            f'Адрес: {instance.address}\n' \
            f'Кол-во персон: {instance.person}\n' \
            f'Комментарий: {instance.comment}\n' \
            f'-----------------------\n' \
            f'Заказ: \n{items}\n' \
            f'-----------------------\n' \
            f'Сумма: {total}'
        vk.messages.send(
            user_id=314252417,
            random_id=get_random_id(),
            message=message
        )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').prefetch_related('ingredients', 'variants').filter(base=None)
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'price',)

    @action(detail=False)
    def short_list(self, request):
        if 'category' in request.query_params:
            category = request.query_params['category']
            products = Product.objects.select_related('category').filter(category_id=category)[:4]
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response(list())


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'pub_shop/category_detail.html'

    def get_object(self):
        return get_object_or_404(Category.objects.prefetch_related('products'), slug__iexact=self.kwargs['slug'])


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pub_shop/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product.objects.select_related('category'), slug__iexact=self.kwargs['product_slug'])


class CartPage(TemplateView):
    template_name = 'pages/cart.html'
