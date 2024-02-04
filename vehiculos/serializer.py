from django.contrib.auth.models import User
from rest_framework import serializers

from vehiculos.models import Marca, Vehiculo

"""
La serialización en DRF se utiliza para convertir datos complejos, como objetos de modelos de Django, en un formato que 
pueda ser fácilmente representado y consumido, como JSON.
"""


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='marca-highlight', format='html')

    class Meta:
        model = Marca
        fields = ['nombre', 'highlight']


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    marca = serializers.HyperlinkedRelatedField(view_name='marca-detail', queryset=Marca.objects.all())

    class Meta:
        model = Vehiculo
        fields = ['tipo_vehiculo', 'color', 'marca', 'chasis', 'modelo', 'fecha_matriculacion',
                  'fecha_fabricacion', 'fecha_baja', 'matricula', 'suspendido']

