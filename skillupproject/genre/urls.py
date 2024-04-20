from django.urls import path
from genre import views

urlpatterns = [
    path("",views.index,name='index'),
    path("genre/<genre_id>",views.details,name='details')
]