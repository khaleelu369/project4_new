from django.urls import path
from . import views
urlpatterns = [
    path('mycart',views.mycart),  
    path('myorder',views.myorder)  
   
]    