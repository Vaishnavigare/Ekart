from django.urls import path
from ecomapp import views

urlpatterns =[  
    path('',views.home),
   # path('register',views.register),
    #path('login',views.login),
    path('base',views.reuse),
    path('sort/<sv>',views.sort),
    path('catfilter/<catv>',views.catfilter),
    path('pricefilter/<pv>',views.pricefilter),
    path('pricerange',views.pricerange),
    path('pdetails/<pid>',views.product_details),
    path('addproduct',views.addproduct),
    path('delproduct/<rid>',views.delproduct),
    path('editproduct/<rid>',views.editproduct),
    path('djangoform',views.djangoform),
    path('modelform',views.modelform),
    path('user_register',views.user_register),
    path('user_login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('cart/<pid>',views.addtocart),
    path('logout',views.user_logout),
    path('viewcart',views.viewcart),
    path('changeqty/<pid>/<f>',views.changeqty),
    path('remove/<rid>',views.remove),
    path('placeorder',views.placeorder),
    path('payment',views.payment),
    path('store',views.storedetails),
]
