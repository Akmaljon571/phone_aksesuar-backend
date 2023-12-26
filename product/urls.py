from django.urls import path

from .views import ProductListByCategoryAndUser

urlpatterns = [
    path('<int:category_id>/user/<int:user_id>/', ProductListByCategoryAndUser.as_view()),
]
