from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name = 'blog-home'),
    path('new/',views.news , name = 'new'),
    path('register/', views.register, name='register'),

]
