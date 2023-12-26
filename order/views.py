from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OrderModel
from .serializers import OrderSerializer


class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        likes = OrderModel.objects.filter(user_id=user_id)
        serializer = OrderSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Like created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        try:
            order = OrderModel.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        action = request.data.get('action')  # 'increment' or 'decrement'

        if action == 'increment':
            order.count += 1
        elif action == 'decrement':
            if order.count > 0:
                order.count -= 1
            else:
                return Response({'error': 'Count cannot be negative'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        pro_id = kwargs.get('pro_id')
        user_id = request.data.get('user_id')
        try:
            like = OrderModel.objects.get(post_id=pro_id, user_id=user_id)
            like.delete()
            return Response({'message': 'Like deleted successfully'})
        except OrderModel.DoesNotExist:
            return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)