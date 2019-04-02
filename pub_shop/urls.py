from django.urls import path
from .views import CategoryDetail

urlpatterns = [
    path('<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
]