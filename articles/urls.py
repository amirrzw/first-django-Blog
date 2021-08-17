from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles'
urlpatterns = [
    path('', views.articles_list, name="list"),
    path('<slug>', views.article_detail, name="detail"),
]

urlpatterns += staticfiles_urlpatterns()
