from . import views
from django.urls import path

urlpatterns = [
    # main pages
    path('', views.index_main, name='main_home'),
    path('services/', views.index_services, name='main_services'),
    path('shop/', views.ProductList.as_view(), name='main_shop'),
    path('contact/', views.CreateReview.as_view(), name='main_contact'),
    path('about/', views.index_about, name='main_about'),
    path('about_detail/', views.about_detail, name='about_detail'),

    # products
    path('category/<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('shop-category/<slug:slug>/', views.ProductListBycategory.as_view(), name='shop_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('product/<slug:slug>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<slug:slug>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('product_cart/', views.ProductCartList.as_view(), name='product_cart'),
    path('order_products/', views.order_products, name='order_products'),
    path('add_to_cart/<slug:slug>', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:pk>', views.DeleteCartItem.as_view(), name='delete_from_cart')
]

