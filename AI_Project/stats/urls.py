from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('descriptives/', views.descriptives, name='descriptives'),
    path('denombrement/', views.denombrement, name='denombrement'),
    path('probabilites/', views.probabilites, name='probabilites'),
]