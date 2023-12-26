from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LikeSerializer
from .models import LikeModel


class LikeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        likes = LikeModel.objects.filter(user_id=user_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Like created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pro_id = kwargs.get('pro_id')
        user_id = request.data.get('user_id')  # Assuming you send user_id in the request data
        try:
            like = LikeModel.objects.get(post_id=pro_id, user_id=user_id)
            like.delete()
            return Response({'message': 'Like deleted successfully'})
        except LikeModel.DoesNotExist:
            return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)
