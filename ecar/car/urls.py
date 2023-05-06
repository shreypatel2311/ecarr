
from django.urls import path,include
from .views import * 
from . import views
urlpatterns = [
    
    path('cartype/create/',CarTypeCreationView.as_view(),name='cartype_creation'),
    path('cartype/list/',CarTypeListView.as_view(),name='cartype_list'),
    path('cartype/delete/<int:pk>',CarTypeDeleteView.as_view(),name='cartype_delete'),
    path('cartype/update/<int:pk>',CarTypeUpdateView.as_view(),name='cartype_update'),
    path('cartype/detail/<int:pk>',CarTypeDetailView.as_view(),name='cartype_detail'),

    path('varient/create/',CarVarientCreationView.as_view(),name='varient_creation'),
    path('varient/list/',CarVarientListView.as_view(),name='varient_list'),
    path('varient/delete/<int:pk>',CarVarientDeleteView.as_view(),name='varient_delete'),
    path('varient/update/<int:pk>',CarVarientUpdateView.as_view(),name='varient_update'),
    path('varient/detail/<int:pk>',CarVarientDetailView.as_view(),name='varient_detail'),

    path('engine/create/',CarEngineAndTransmissionCreationView.as_view(),name='engine_creation'),
    path('engine/list/',CarEngineAndTransmissionListView.as_view(),name='engine_list'),
    path('engine/delete/<int:pk>',CarEngineAndTransmissionDeleteView.as_view(),name='engine_delete'),
    path('engine/update/<int:pk>',CarEngineAndTransmissionUpdateView.as_view(),name='engine_update'),
    path('engine/detail/<int:pk>',CarEngineAndTransmissionDetailView.as_view(),name='engine_detail'),

    path('brand/create/',BrandCreationView.as_view(),name='brand_creation'),
    path('brand/list/',BrandListView.as_view(),name='brand_list'),
    path('brand/delete/<int:pk>',BrandDeleteView.as_view(),name='brand_delete'),
    path('brand/update/<int:pk>',BrandUpdateView.as_view(),name='brand_update'),
    path('brand/detail/<int:pk>',BrandDetailView.as_view(),name='brand_detail'),

    path('fuel/create/',FuelCreationView.as_view(),name='fuel_creation'),
    path('fuel/list/',FuelListView.as_view(),name='fuel_list'),
    path('fuel/delete/<int:pk>',FuelDeleteView.as_view(),name='fuel_delete'),
    path('fuel/update/<int:pk>',FuelUpdateView.as_view(),name='fuel_update'),
    path('fuel/detail/<int:pk>',FuelDetailView.as_view(),name='fuel_detail'),

    path('exterior/create/',ExteriorCreationView.as_view(),name='exterior_creation'),
    path('exterior/list/',ExteriorListView.as_view(),name='exterior_list'),
    path('exterior/delete/<int:pk>',ExteriorDeleteView.as_view(),name='exterior_delete'),
    path('exterior/update/<int:pk>',ExteriorUpdateView.as_view(),name='exterior_update'),
    path('exterior/detail/<int:pk>',ExteriorDetailView.as_view(),name='exterior_detail'),

    path('car/create/',CarCreationView.as_view(),name='car_creation'),
    path('car/list/',CarListView.as_view(),name='car_list'),
    path('car/delete/<int:pk>',CarDeleteView.as_view(),name='car_delete'),
    path('car/update/<int:pk>',CarUpdateView.as_view(),name='car_update'),
    path('car/detail/<int:pk>',CarDetailView.as_view(),name='car_detail'),

    path('search/',views.search,name='search'),
    path('home/',views.home,name='home')
]