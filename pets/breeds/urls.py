from django.urls import path
from . import views

# Create your tests here.

urlpatterns = [
    path('get_breedlist', views.get_breedlist, name='get_breedlist'),
    path('post_breedlist', views.post_breedlist, name='post_breedlist'),
    path('get_breeddetail', views.get_breeddetail, name='get_breeddetail'),
    path('put_breeddetail', views.put_breeddetail, name='put_breeddetail'),
    path('delete_breeddetail', views.delete_breeddetail, name='delete_breeddetail'),
]