import django_filters.rest_framework
from rest_framework import generics, viewsets
from rest_framework import permissions
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from vehiculos.models import Vehiculo, Marca
from vehiculos.serializer import VehiculoSerializer, MarcaSerializer


# MARCA #
class MarcaViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [permissions.isAuthenticated]
        return [permission() for permission in permission_classes]


# VEHICULO #

class VehiculoViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Filtros Django Filter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # Forma rápida
    filterset_fields = ['marca']

    # Por ruta
    # path("vehiculos/<str: marca>", views.VehiculoViewSet.as_view({'get': 'list'})),
    def get_queryset(self):
        marca = self.kwargs.get('marca', None)
        vehiculos = Vehiculo.objects.all()
        if marca:
            vehiculos = vehiculos.filter(marca__nombre=marca)
        return vehiculos

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(name='marca', description='Filtro por marca', required=False, type=str)
    #     ]
    # )
    # # Filtrar por marca // por query params que debe hacerse con filterset_fields
    # @action(detail=False, methods=['GET'], description='Filtrado por marca get parametro')
    # def filtro_marca(self, request):
    #     vehiculos_marca = Vehiculo.object.all()
    #     marca = self.request.query_params.get('marca')
    #     if (marca):
    #         vehiculos_marca = vehiculos_marca.filter(marca__nombre=marca)
    #
    #     serializer = self.get_serializer(vehiculos_marca, many=True)
    #     return Response(serializer.data)
