from django.urls import path
from . import views

app_name='customer'

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('viewproducts/',views.viewproducts,name='viewproducts'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart , name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('search/', views.search, name='search'),
    path('logout/', views.logout, name='logout'),



]
