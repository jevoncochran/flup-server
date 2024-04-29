from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationListCreate.as_view(), name='applications'),
    path('/<int:pk>/', views.ApplicationDelete.as_view(), name='delete_application')
]