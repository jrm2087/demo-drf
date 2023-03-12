from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from apps.user.api.views import MyTokenObtainPairView

from .views import UserApiViewSet

urlpatterns = [
    path('auth/login/', MyTokenObtainPairView.as_view()),
    path('auth/login/token/refresh/', TokenRefreshView.as_view()),
]

# ViewSet
router_user = DefaultRouter()
router_user.register(prefix='user', basename='user', viewset=UserApiViewSet)
