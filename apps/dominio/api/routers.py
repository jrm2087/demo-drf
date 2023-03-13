from rest_framework.routers import DefaultRouter

from apps.dominio.api.views import DominioApiViewSet

router_dominio = DefaultRouter()
router_dominio.register(prefix='dominio', basename='dominio', viewset=DominioApiViewSet)
