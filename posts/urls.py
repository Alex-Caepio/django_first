from django.urls import path
from .views import PostView, DetailedPost

urlpatterns = [
    path('all/<int:post_id>', PostView.as_view(), name='posts'),
    path('new/', PostView.as_view(), name='create_post'),
    path('<int:post_id>/', DetailedPost.as_view(), name='get_one_post'),
    # path('<int:post_id>/exists/', views.check_if_exists, name='check_if_exists'),
    path('<int:post_id>/update/', DetailedPost.as_view(), name='update_post'),
    path('<int:post_id>/delete/', DetailedPost.as_view(), name='delete_post'),
    # path('<int:post_id>/get_or_create/', views.get_or_create, name='get_or_create'),
    # path('<int:post_id>/update_or_create/', views.update_or_create, name='update_or_create'),
    # path('filter_and_update/', views.filter_and_update, name='filter_and_update'),
    # path('get_all_posts/', views.get_all_posts, name='get_all_posts'),
    # path('create_comment/', views.create_comment, name='create_comment'),
    # path('get_comment_by_post/<int:posts_id>', views.get_comment_by_post, name='get_comment_by_post'),
    # path('change_comment_status/<int:post_id>/<str:status>', views.change_status_comment_by_post_id,
    #      name='change_status_comment_by_post_id'),
    path('get', PostView.as_view(), name='get'),
]
