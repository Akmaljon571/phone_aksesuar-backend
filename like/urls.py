from django.urls import path

from .views import *

urlpatterns = [
    path('', LikeCreate.as_view()),
    path('user/<int:user_id>/', LikeAPIView.as_view()),
    path('user/<int:user_id>/pro/<int:pro_id>', LikeDelete.as_view())
]
