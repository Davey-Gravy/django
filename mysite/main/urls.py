from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name='Index'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='Create'),
    path('view/', views.view, name='view')
]
