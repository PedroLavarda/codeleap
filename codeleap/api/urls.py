from django.urls import path
from .views import posts_view, post_detail_view, comments_view_by_post, signup_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', posts_view, name='posts_view'),
    path('<int:post_id>/', post_detail_view, name='post_detail'),
    path('<int:post_id>/comments/', comments_view_by_post, name='comments_view_by_post'),
    path('auth/login/', obtain_auth_token, name='login_view'),
    path('auth/logout/', comments_view_by_post, name='logout_view'),
    path('auth/signup/', signup_view, name='signup_view'),
]
