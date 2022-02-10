from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aqua/', include('aqua.urls')),
    path('blue/', include('blue.urls')),
]
