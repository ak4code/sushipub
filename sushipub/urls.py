"""sushipub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path, include
from pub_main.views import PageDetail, HomePage, OrderView
from pub_shop.views import CartPage
from .api import router

admin.site.site_title = 'Sushi Pub - Админ панель'
admin.site.site_header = 'Sushi Pub'
admin.site.index_title = 'Sushi Pub - Админ панель'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/', include(router.urls)),
    path('menu/', include('pub_shop.urls')),
    path('accounts/login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('cart/', CartPage.as_view(), name='cart'),
    path('orders/', login_required(OrderView.as_view()), name='orders'),
    path('', HomePage.as_view(), name='home'),
    path('<slug:slug>/', PageDetail.as_view(), name='page')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
