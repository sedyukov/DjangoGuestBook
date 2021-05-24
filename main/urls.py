from django.urls import path
from django.conf.urls import include
from . import views


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
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('register', views.register, name='register'),
    path('<int:pk>/update', views.ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete', views.ReviewDeleteView.as_view(), name='review-delete')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
