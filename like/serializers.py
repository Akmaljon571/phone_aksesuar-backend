from rest_framework import serializers

from .models import LikeModel
from product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    pro_id = ProductSerializer()

    class Meta:
        model = LikeModel
        fields = ('id', 'pro_id', 'user_id')

