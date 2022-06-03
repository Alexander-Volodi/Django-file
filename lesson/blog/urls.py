from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/sign_up/', views.sign_up, name='sign_up'),
    path('post/sign_in/', views.sign_in, name='sign_in'),
]
