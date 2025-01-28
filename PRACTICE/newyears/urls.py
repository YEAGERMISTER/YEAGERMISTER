from newyears import views
from django.urls import path

urlpatterns = [
    path('newyears/', views.index, name = 'newyears'),
]