from django.urls import path

from .views import PostDetail, PostList

app_name = 'blogapi'

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail')
]
