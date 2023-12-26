from django.urls import path

from .views import OrderAPIView

urlpatterns = [
    path('user/<int:user_id>', OrderAPIView.as_view()),
    path('user/<int:user_id>/pro/<int:pro_id>', OrderAPIView.as_view()),
    path('count/<int:order_id>', OrderAPIView.as_view()),
]
