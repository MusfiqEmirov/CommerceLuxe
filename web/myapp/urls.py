from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="product-edit"),
    path('delete/<int:id>/', views.delete, name="product-delete"),
    path('upload/', views.upload, name="upload-image"),
    path('<slug:slug>/', views.detalis,name="products_detalis"),

]


