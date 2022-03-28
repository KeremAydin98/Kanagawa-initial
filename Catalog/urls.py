from django.urls import path
from .views import HomePageView, AboutPageView,DetailPageView, CreatePageView, UpdatePageView, DeletePageView

urlpatterns = [
    path('Catalog/<int:pk>/delete/', DeletePageView.as_view(), name='product_delete'),
    path('Catalog/new/', CreatePageView.as_view(), name='product_new'),
    path('Catalog/<int:pk>/', DetailPageView.as_view(), name='product_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('Catalog/<int:pk>/edit/', UpdatePageView.as_view(), name='product_edit'),
    path('about/', AboutPageView.as_view(), name='about'),
]