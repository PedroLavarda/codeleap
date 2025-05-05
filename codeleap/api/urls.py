from django.urls import path
from .views import posts_view, post_detail_view, comments_view_by_post

urlpatterns = [
    path('', posts_view, name='posts_view'),
    path('<int:post_id>/', post_detail_view, name='post_detail'),
    path('<int:post_id>/comments/', comments_view_by_post, name='comments_view_by_post'),
]
