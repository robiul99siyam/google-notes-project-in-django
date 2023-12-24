from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('profile/' , include('profiles.urls')),
    path('', views.home,name='home')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
