from django.urls import path
from .import views
app_name='regapp'
urlpatterns=[
path('',views.index,name='index'),
path('register',views.register,name='register'),
path('symptoms',views.symp,name='symp'),
path('shop',views.shop,name='shop'),
path('research',views.res,name='res')


]