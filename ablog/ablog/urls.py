
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('signup/', include('django.contrib.auth.urls')),
    path('signup/', include('signup.urls')),
        
    
]
