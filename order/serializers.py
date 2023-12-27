from rest_framework.serializers import ModelSerializer

from .models import OrderModel
from like.serializers import ProductSerializer


class OrderSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderCreateSerializer(ModelSerializer):

    class Meta:
        model = OrderModel
        fields = '__all__'
