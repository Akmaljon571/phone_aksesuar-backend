from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderCreate.as_view()),
    path('user/<int:user_id>', OrderAPIView.as_view()),
    path('count/<int:order_id>', OrderCount.as_view()),
    path('user/<int:user_id>/pro/<int:pro_id>', OrderDelete.as_view()),
]
