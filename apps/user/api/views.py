from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.user.api.serializers import MyTokenObtainPairSerializer

from .serializers import UserSerializers
from apps.user.models import User
from apps.permissions import CustomPermission


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserApiViewSet(ModelViewSet):
    permission_classes = [CustomPermission]
    serializer_class = UserSerializers
    queryset = User.objects.all()
