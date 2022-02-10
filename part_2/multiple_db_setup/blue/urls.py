from django.urls import path
from . import views

urlpatterns = [
    path('', views.Add.as_view(), name='add-blue'),
    path('view-data/', views.view_data, name='view-blue-data'),
]
