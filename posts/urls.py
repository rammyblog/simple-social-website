from django.urls import path, include
from . import views
app_name = 'post'
urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single'),
    path('by/<username>/<pk>/delete', views.DeletePost.as_view(), name='delete'),

    #path('posts/in/<slug>', views.SingleGroup.as_view(), name='single'),

]