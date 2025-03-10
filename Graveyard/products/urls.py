from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('1', views.helloworld, name="one"),
    path('lezzat', views.alireza),
    path('list', views.list),
]