from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_product, name="all_product"),
    path('<int:pk>/', views.product_by_id, name="product_by_id"),
    path('variant/', views.all_variant, name="all_variant"),
    path('variant/<int:pk>/', views.variant_by_id, name="variant_by_id")
]
