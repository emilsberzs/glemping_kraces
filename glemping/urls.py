from django.urls import path
from . import views

app_name = 'glemping'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('news/', views.post_list, name='post_list'),
    path('news/<slug:post>/', views.post_detail, name='post_detail'),
]
