from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer
from .models import CategoryModel


class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
