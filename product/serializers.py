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
        user = request.user if request and hasattr(request, 'user') else None

        if user and user.is_authenticated:
            return LikeModel.objects.filter(user_id=user.id, pro_id=obj.id).exists()
        return False

    def get_ordered(self, obj):
        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') else None

        if user and user.is_authenticated:
            return OrderModel.objects.filter(user_id=user.id, product_id=obj.id).exists()
        return False
