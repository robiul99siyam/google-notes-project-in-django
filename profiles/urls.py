from django.urls import path , include

from . import views
urlpatterns = [

    path('write/',views.profile,name='profile'),
    path('Reminder/',views.reminder,name='reminder'),
    path('edit<int:id>/',views.data_update.as_view(),name='data_update'),
    path('datashow/',views.temp,name='temp'),
    path('deletenow<int:id>/',views.deleteNow,name='delete'),
   
]
