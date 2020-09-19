from rest_framework import viewsets
from ecommapp.serializers import categoriaSerializer, clienteSerializer, cuponSerializer, detalle_pedidoSerializer, estado_pedidoSerializer, pedidoSerializer, productoSerializer
from ecommapp.models import categoria, cliente, cupon, detalle_pedido, estado_pedido, pedido, producto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from django.http import JsonResponse

# from culqi import __version__
# from culqi.client import Culqi
# from culqi.resources import Charge

from django.views.decorators.csrf import csrf_exempt

import requests

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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
    
def payment(request):
    return render(request, 'payment/index.html')

@csrf_exempt
def charges(request):
    if request.method == 'POST':
        token = request.POST['token']
        installments = request.POST['installments']
        pedido = int(request.POST['idPedido'])
        email = request.POST['email']
        monto = int(request.POST['monto'])
        descrpcion = 'Pago pachaqtec curso online'
        moneda = request.POST['moneda']

        #culqi.secret_key = "sk_test_9nH5LBeMpmnk4qvI"
        auth_token=env("CULQI_AUTH_TOKEN")
        hed = {'Authorization': 'Bearer ' + auth_token}
        data = {
            'amount': monto,
            'currency_code': moneda,
            'email': email,
            'source_id':token,
            'installments':installments,
            'metadata':{'Descripcion': descrpcion}
        }

        url = env("CULQI_URL")
        charge = requests.post(url, json=data, headers=hed)

        logger.debug(charge.json())
        dicRes = {'message':'EXITO'}
        return JsonResponse(charge.json(), safe=False)

    return JsonResponse("only POST method", safe=False)
