from django.urls import path
from . import views

app_name = 'glemping'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('news/', views.post_list, name='post_list'),
    path('news/<slug:post>/', views.post_detail, name='post_detail'),
    path('activities/', views.activity_list, name='activity_list'),
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('reviews/', views.review_view, name='reviews'),
]
