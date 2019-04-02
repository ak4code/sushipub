from rest_framework.routers import DefaultRouter
from pub_shop.views import CategoryViewSet, ProductViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
