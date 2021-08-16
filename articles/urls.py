from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.articles_list),
]

urlpatterns += staticfiles_urlpatterns()