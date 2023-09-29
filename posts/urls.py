from . import views
from django.urls import path

urlpatterns = [
    path('all/<int:post_id>', views.my_posts, name='posts'),
    path('new/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.get_one_post, name='get_one_post'),
    path('<int:post_id>/exists/', views.check_if_exists, name='check_if_exists'),
    path('<int:post_id>/update/', views.update_post, name='update_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('<int:post_id>/get_or_create/', views.get_or_create, name='get_or_create'),
    path('<int:post_id>/update_or_create/', views.update_or_create, name='update_or_create'),
    path('filter_and_update/', views.filter_and_update, name='filter_and_update'),
]
