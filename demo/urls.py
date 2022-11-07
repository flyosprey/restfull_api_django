from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from store import views, api_views

urlpatterns = [
    path('api/v1/products/', api_views.ProductList.as_view()),
    path('api/v1/products/new/', api_views.ProductCreation.as_view()),
    path('api/v1/products/<int:id>/', api_views.ProductRetrieveUpdateCreation.as_view()),

    path('admin/', admin.site.urls),
    path('products/<int:id>/', views.show, name='show-product'),
    path('cart/', views.cart, name='shopping-cart'),
    path('', views.index, name='list-products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
