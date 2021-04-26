from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views
from main.forms import UserLoginForm

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('personal', views.personal),
    path('cowork', views.cowork),
    path('other', views.other),
    path('optimization', views.optimization),
    path('bydate', views.bydate),
    path('byalphauth', views.byalphauth),
    path('byalphtext', views.byalphtext),
    path('exit', views.logout_view),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
