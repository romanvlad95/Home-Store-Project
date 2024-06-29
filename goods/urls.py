
from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalogue, name='search'),
    path('<slug:category_slug>/', views.catalogue, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
