from django.urls import path

from .views import *

urlpatterns = [
    path('<int:user_id>/', LikeAPIView.as_view())
]
