from rest_framework import status, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse

from vehiculos.models import Vehiculo, Marca
from vehiculos.serializer import VehiculoSerializer, MarcaSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'marcas': reverse('marca-list', request=request, format=format),
        'vehiculos': reverse('vehiculo-list', request=request, format=format)
    })


# MARCA #
class MarcaList(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class MarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class MarcaHighlight(generics.GenericAPIView):
    queryset = Marca.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        marca = self.get_object()
        return Response(marca.highlighted)


# VEHICULO #

class VehiculoList(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class VehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class VehiculoHighlight(generics.GenericAPIView):
    queryset = Vehiculo.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        vehiculo = self.get_object()
        return Response(vehiculo.highlighted)
