from django.urls import path,include
from sub_part import views

urlpatterns=[
    path('',views.index,name='index'),
    path('first',views.first,name='first'),

]