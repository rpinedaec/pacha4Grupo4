"""ecommprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from ecommapp import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework import routers

from allauth.account.views import confirm_email

from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'categoria', views.categoriaViewSet, basename = 'categoria')
router.register(r'cliente', views.clienteViewSet, basename = 'cliente')
router.register(r'cupon', views.cuponViewSet, basename = 'cupon')
router.register(r'detalle_pedido', views.detalle_pedidoViewSet, basename = 'detalle_pedido')
router.register(r'estado_pedido', views.estado_pedidoViewSet, basename = 'estado_pedido')
router.register(r'pedido', views.pedidoViewSet, basename = 'pedido')
router.register(r'producto', views.productoViewSet, basename = 'producto')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
 #   url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
