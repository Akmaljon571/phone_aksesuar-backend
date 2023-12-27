from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LikeSerializer, LikeCreateSerializer
from .models import LikeModel


class LikeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        likes = LikeModel.objects.filter(user_id=user_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)


class LikeCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LikeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Like created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDelete(APIView):
    def delete(self, request, *args, **kwargs):
        pro_id = kwargs.get('pro_id')
        user_id = kwargs.get('user_id')
        try:
            like = LikeModel.objects.filter(pro_id=pro_id, user_id=user_id)
            like.delete()
            return Response({'message': 'Like deleted successfully'})
        except LikeModel.DoesNotExist:
            return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)
