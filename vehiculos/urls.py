from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehiculos import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'marcas', views.MarcaViewSet, basename='marca')
router.register(r'vehiculos', views.VehiculoViewSet, basename='vehiculo')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path("vehiculos/<str: marca>/", views.VehiculoViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
]