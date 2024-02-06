from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from vehiculos.models import Vehiculo, Marca
from vehiculos.serializer import VehiculoSerializer, MarcaSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'marcas': reverse('marca-list', request=request, format=format),
        'vehiculos': reverse('vehiculo-list', request=request, format=format)
    })


# MARCA #
class MarcaViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        marca = self.get_object()
        return Response(marca.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# VEHICULO #

class VehiculoViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        vehiculo = self.get_object()
        return Response(vehiculo.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

