from rest_framework import generics
from django.db.models import Exists, OuterRef
from .models import ProductModel
from .serializers import ProductSerializer
from like.models import LikeModel
from order.models import OrderModel


class ProductListByCategoryAndUser(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        user_id = self.kwargs.get('user_id')

        queryset = ProductModel.objects.filter(cat_id=category_id)

        if user_id:
            queryset = queryset.annotate(
                liked=Exists(LikeModel.objects.filter(user_id=user_id, pro_id=OuterRef('id'))),
                ordered=Exists(OrderModel.objects.filter(user=user_id, product=OuterRef('id')))
            )

        return queryset
