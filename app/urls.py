from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name="post_detail"),
    path('add/', views.post_add, name="post_add"),
]