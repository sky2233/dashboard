from django.urls import path
from django.contrib import admin

from . import views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', views.get, name='main'),
    path('details/', views.details, name='details'),
    path('details/postComments', views.comments, name='post comments'),
    path('details/deleteComments/<str:commentID>/', views.comments, name='post comments'),
]