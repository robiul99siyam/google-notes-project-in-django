from django.urls import path , include

from . import views
urlpatterns = [

    path('Register/', views.Register.as_view() , name='register'),
    path('login/', views.login.as_view() , name='login'),
    path('logout/', views.logout.as_view() , name='logout'),
    path('image/', views.image.as_view(),name='image'),
    path('user/updata/<int:id>/', views.upadate.as_view(),name='update'),
    path('password/', views.password,name='pass')
    
   
]
