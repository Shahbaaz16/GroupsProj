#POSTS URLS.py file
from django.urls import path, re_path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('create/',views.CreatePost.as_view(),name='create'),
    path('by/<username>',views.UserPosts.as_view(),name='for_user'),
    path('by/<username>/<int:pk>/',views.PostDetail.as_view(),name='single'),
    path('delete/<int:pk>/',views.DeletePost.as_view(),name='delete')
    # re_path(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    # re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    # re_path(r'delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete')
]
