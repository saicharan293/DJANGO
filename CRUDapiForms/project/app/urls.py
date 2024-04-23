from django.urls import path
from app import views

urlpatterns = [
    path("",views.index,name='index'),
    # path("add_show",views.add_show,name='insertData'),
]