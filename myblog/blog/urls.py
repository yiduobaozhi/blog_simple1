from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'index/', views.index),
    path(r'article/<int:article_id>/', views.page_article),
    path(r'edit/<int:article_id>/', views.edit_page),
    path(r'edit/action', views.edit_action),
   # re_path('^article/(?P<article_id>[0-9]+)$', views.page_article)
]