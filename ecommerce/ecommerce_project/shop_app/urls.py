from . import views
from django.urls import path

app_name = 'shop_app'

urlpatterns = [
    path('', views.allProductCat, name='allProductCat'),
    path('<slug:cat_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:cat_slug>/<slug:pro_slug>/', views.proDetail, name='procatDetail'),
]
