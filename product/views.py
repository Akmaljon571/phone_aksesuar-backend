from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import ProductModel
from .serializers import ProductSerializer


class ProductAllView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
