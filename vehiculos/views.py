from django_filters.rest_framework import DjangoFilterBackend
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


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
    filter_backends = DjangoFilterBackend
    # Forma rápida
    filterset_fields = ['marca']
    @extend_schema(
        parameters=[
            OpenApiParameter(name='marca', description='Filtro por marca', require=False, type=str)
        ]
    )
    # Filtrar por marca // por query
    @action(detail=False, methods=['GET'], description='Filtrado por marca get parametro')
    def filtro_marca(self, request):
        vehiculos_marca = Vehiculo.object.all()
        marca = self.request.query_params.get('marca')
        if (marca):
            vehiculos_marca = vehiculos_marca.filter(marca__nombre=marca)

        serializer = self.get_serializer(vehiculos_marca, many=True)
        return Response(serializer.data)
