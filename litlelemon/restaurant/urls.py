from django.contrib import admin 
from django.urls import path, include
from .views import *
from . import views

  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]