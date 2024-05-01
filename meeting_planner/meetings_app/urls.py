from django.urls import path

from meetings_app.views import meeting_details_view,rooms_view

urlpatterns = [
    path('<int:id>',meeting_details_view,name='detail'),
    path('rooms',rooms_view,name='rooms')
]
