# serializers.py
from rest_framework import serializers
from .models import ProductModel
from like.models import LikeModel
from order.models import OrderModel


class ProductSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField()
    ordered = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'price', 'image', 'cat_id', 'liked', 'ordered']

    def get_liked(self, obj):
        request = self.context.get('request')
        user = str(request).split('/')[-2]
        if user:
            return LikeModel.objects.filter(user_id=user, pro_id=obj.id).exists()
        return False

    def get_ordered(self, obj):
        request = self.context.get('request')
        user = str(request).split('/')[-2]
        if user:
            return OrderModel.objects.filter(user=user, product=obj.id).exists()
        return False
