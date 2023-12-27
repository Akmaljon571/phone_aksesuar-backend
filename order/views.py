from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OrderModel
from .serializers import OrderSerializer, OrderCreateSerializer


class OrderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        orders = OrderModel.objects.filter(user_id=user_id)
        serializer = OrderSerializer(orders, many=True)
        jami = 0

        for a in serializer.data:
            jami += int(a['product']['price']) * int(a["count"])

        return Response({"data": serializer.data, "jami": jami})


class OrderCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Order created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAddCount(APIView):
    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        try:
            order = OrderModel.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        order.count += 1

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderDepletionCount(APIView):
    def put(self, request, *args, **kwargs):
        order_id = kwargs.get('order_id')
        try:
            order = OrderModel.objects.get(id=order_id)
        except OrderModel.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        if order.count > 1:
            order.count -= 1

            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        return Response({'error': 'Order count == 1'}, status=status.HTTP_404_NOT_FOUND)


class OrderDelete(APIView):
    def delete(self, request, *args, **kwargs):
        pro_id = kwargs.get('pro_id')
        user_id = kwargs.get('user_id')
        try:
            order = OrderModel.objects.filter(product=pro_id, user_id=user_id)
            order.delete()
            return Response({'message': 'Order deleted successfully'})
        except OrderModel.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
