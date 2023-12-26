from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from auth.views import UserRegistrationView, UserLoginView, UserData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('like/', include('like.urls')),
    path('order/', include('order.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/register/', UserRegistrationView.as_view()),
    path('api/login/', UserLoginView.as_view()),
    path('api/data/<int:pk>', UserData.as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
