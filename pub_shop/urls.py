from django.urls import path
from .views import CategoryDetail, ProductDetail

urlpatterns = [
    path('<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-detail'),
]