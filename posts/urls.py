from django.urls import path
from posts import views
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<str:pk>',views.post,name='posts'),
    path('write',views.blogpost,name='write_blog')
]
