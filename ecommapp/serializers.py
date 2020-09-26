from rest_framework import serializers

from ecommapp.models import categoria, cliente, cupon, detalle_pedido, estado_pedido, pedido, producto


class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class cuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = cupon
        fields = '__all__'
class detalle_pedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = detalle_pedido
        fields = '__all__'
class estado_pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estado_pedido
        fields = '__all__'



class pedidoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = pedido
        fields = '__all__'

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'