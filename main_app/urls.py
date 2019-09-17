from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemIndex.as_view(), name='items_index'),
    path('add/', views.ItemCreate.as_view(), name='items_create'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]
