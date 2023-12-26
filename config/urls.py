from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from auth.views import UserRegistrationView, UserLoginView, UserData

schema_view = get_schema_view(
    openapi.Info(
        title="Phone Aksessuar",
        default_version='v1',
        description="Telefon aksessuarlar sotiladigan magazin",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('like/', include('like.urls')),
    path('order/', include('order.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', UserRegistrationView.as_view()),
    path('api/login/', UserLoginView.as_view()),
    path('api/data/<int:pk>', UserData.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )