from django.contrib import admin
from django.urls import path
from book.views import examples

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', examples, name='home')
]
