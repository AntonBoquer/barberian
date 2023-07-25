from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("products/", views.products, name='products'),
    path("inventory/", views.inventory, name='inventory'),
    path("service/", views.service, name='service'),
    path("drinks/", views.service),
    path("", views.loginPage, name='login'),
   
   


    path("products/addproduct/", views.addproduct),
    path("products/removeproduct/", views.removeproduct),
    path("service/addservice/", views.addservice),
    path("service/removeservice/", views.removeservice),
    path("service/update/<int:id>", views.update, name='update'),
    path('service/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path("products/updateDrink/<int:id>", views.updateDrink, name='updateDrink'),
    path('products/updaterecord/<int:id>', views.updaterecordDrink, name='updaterecordDrink'),

]
