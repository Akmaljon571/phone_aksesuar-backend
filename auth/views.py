# views.py
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from like.models import LikeModel
from order.models import OrderModel
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate the access token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Include the access token in the response
        response_data = {
            'access_token': access_token,
            'user_id': user.id,  # You can include additional user-related information
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=self.request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            # Generate the access token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Include the access token in the response
            response_data = {
                'access_token': access_token,
                'user_id': user.id,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserData(APIView):
    def get(self, request, pk):
        order_count = OrderModel.objects.filter(user_id=pk).count()
        like_count = LikeModel.objects.filter(user_id=pk).count()

        response_data = {
            'order_count': order_count,
            'like_count': like_count,
        }

        return Response(response_data, status=status.HTTP_200_OK)
