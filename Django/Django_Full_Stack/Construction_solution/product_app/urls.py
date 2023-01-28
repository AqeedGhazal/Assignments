from django.urls import path 
from . import views


urlpatterns = [
    path('', views.mainpage ),
    path('reg', views.Log_reg),
    path('regestireuser' , views.register_user),
    path ('regestireengineer' , views.register_engineer),
    path('products', views.success_login_eng),
    path('login' , views.login_engineer),
    path('addproduct' , views.create_product),
    path('allproducts', views.success_login_user),
    path('loginuser' , views.login_user),
    path('logout' , views.logout_user), 
    path('allproducts_eng' , views.showproductseng),
    path ('showproduct/<int:product_id>' , views.show_product),
    path ('showproductuser/<int:product_id>' , views.show_product_user),
    path ('showproduct/<int:product_id>/addaltproduct', views.create_altr_product), 
    path ('showproduct/<int:product_id>/<int:altr_product_id>/delete' , views.delete_altr_product),
    path('showproduct/<int:product_id>/addreview' , views.user_addreview),
    path('showproductuser/<int:product_id>/<int:review_id>/delete' ,views.user_deletereview),
    path('engineers/<int:engineer_id>' , views.engineer_info),
    path('showproduct/<int:product_id>/addengreview' , views.eng_addreview),
]