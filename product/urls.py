from django.urls import path

from .views import ProductAllView

urlpatterns = [
    path('', ProductAllView.as_view())
]
