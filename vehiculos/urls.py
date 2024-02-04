from django.urls import path, include

from vehiculos import views

urlpatterns = [
    path('', views.api_root),
    path('marcas/<int:pk>/highlight/', views.MarcaHighlight.as_view(), name='marca-highlight'),
    path('vehiculos/<int:pk>/highlight/', views.VehiculoHighlight.as_view(), name='vehiculo-highlight'),
    path('marcas/', views.MarcaList.as_view(), name='marca-list'),
    path('marcas/<int:pk>/', views.MarcaDetail.as_view(), name='marca-detail'),
    path('vehiculos/', views.VehiculoList.as_view(), name='vehiculo-list'),
    path('vehiculos/<int:pk>/', views.VehiculoDetail.as_view(), name='vehiculo-detail'),

]