from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('personal', views.personal),
    path('cowork', views.cowork),
    path('other', views.other),
    path('optimization', views.optimization),
]