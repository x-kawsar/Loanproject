from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create-wing', views.create_wing_one, name='create-wing'),
]