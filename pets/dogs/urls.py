from django.urls import path
from . import views

# Create your tests here.

urlpatterns = [
    path('', views.base, name='views.base'),
    path('get_doglist', views.get_doglist, name='get_doglist'),
    path('post_doglist', views.post_doglist, name='post_doglist'),
    path('get_dogdetail', views.get_dogdetail, name='get_dogdetail'),
    path('put_dogdetail', views.put_dogdetail, name='put_dogdetail'),
    path('delete_dogdetail', views.delete_dogdetail, name='delete_dogdetail'),
]