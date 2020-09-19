from django.contrib import admin
from django.urls import include, path
from ecommapp import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework import routers

from allauth.account.views import confirm_email

from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="PachaQtec Hackaton Final Grupo 4",
      default_version='v1',
      description="Descripcion de APIS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^charges/', views.charges, name='charges'),
]
