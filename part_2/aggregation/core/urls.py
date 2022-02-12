from django.contrib import admin
from django.urls import path, include
from book.views import examples

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', examples, name='home'),
]
