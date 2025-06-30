from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('1', views.helloworld, name="one"),
    path('lezzat', views.alireza),
    path('list', views.list, name="list"),
    path('form1', views.form1, name="form1"),
    path('form1/<int:errno>', views.form1, name="form1"),
    path('detail/<int:product_id>', views.detail, name="detail"),
    path('delete/<int:product_id>', views.delete, name="delete"),
    path('api/list', views.testdrf, name="apilist"),
]
 