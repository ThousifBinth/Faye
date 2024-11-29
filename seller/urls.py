from django.urls import path
from . import views

app_name='seller'

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('addproducts/<int:category_id>',views.addproducts,name='addproducts'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('viewproducts/',views.viewproducts,name='viewproducts'),
    path('maincat/',views.maincat,name='maincat'),
    path('deleteproducts/<int:id>',views.deleteproducts,name='deleteproducts'),
    path('editproducts/<int:id>',views.editproducts,name='editproducts'),


   
]
