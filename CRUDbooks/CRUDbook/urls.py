
from django.urls import path
from .views import *

urlpatterns = [
    path('',Booklist),
    path('add/',post_book),
    path('update/<id>',update_book),
    path('delete/<id>',delete_book)
]