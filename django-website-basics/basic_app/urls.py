from django.contrib import admin
from django.urls import path
from basic_app import views

# TEMPLATE TAGGING

# app_name = 'basic_app' -> tell django look under the basic app and then find the URL that matches
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('admin/', admin.site.urls),
]
