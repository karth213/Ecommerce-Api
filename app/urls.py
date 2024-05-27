from django.urls import path, include 

from . views import ProductView, CategoryView
from app import views

urlpatterns = [
    path('Pr/', ProductView.as_view(), name = 'pro'),
    path('Pr/search/', views.search),
    path('prducts/<slug:category_slug>/', CategoryView.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductView.as_view()),

]