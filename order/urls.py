from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderCreate.as_view()),
    path('user/<int:user_id>', OrderAPIView.as_view()),
    path('add/<int:order_id>', OrderAddCount.as_view()),
    path('depletion/<int:order_id>', OrderDepletionCount.as_view()),
    path('user/<int:user_id>/pro/<int:pro_id>', OrderDelete.as_view()),
]
