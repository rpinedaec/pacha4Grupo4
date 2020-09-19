from rest_framework import viewsets
from ecommapp.serializers import categoriaSerializer, clienteSerializer, cuponSerializer, detalle_pedidoSerializer, estado_pedidoSerializer, pedidoSerializer, productoSerializer
from ecommapp.models import categoria, cliente, cupon, detalle_pedido, estado_pedido, pedido, producto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class categoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre','descripcion',]

    # def get_queryset(self):
    #     queryset = categoria.objects.all()
    #     nombre = self.request.query_params.get('nombre',None)
    #     if desc is not None:
    #         queryset = queryset.filter(nombre=nombre)
    #     return queryset
class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['username','email',]
    
class cuponViewSet(viewsets.ModelViewSet):
    queryset = cupon.objects.all()
    serializer_class = cuponSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['codigo','descripcion', 'descuento',]
    
class detalle_pedidoViewSet(viewsets.ModelViewSet):
    queryset = detalle_pedido.objects.all()
    serializer_class = detalle_pedidoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['id',]
    
class estado_pedidoViewSet(viewsets.ModelViewSet):
    queryset = estado_pedido.objects.all()
    serializer_class = estado_pedidoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['descripcion',]
    
class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    serializer_class = pedidoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['cliente', 'estado',]
    
class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter]
    search_fields=['nombre','descripcion','categoria']
    

