#Groups URLS.py file
from django.urls import path, re_path
from groups import views

app_name = 'groups'

urlpatterns = [
    path('',views.ListGroups.as_view(),name='all'),
    path('create',views.CreateGroup.as_view(),name='create'),
    path('post/in/<slug:slug>',views.SingleGroup.as_view(),name='single'),
    # re_path('posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    path('join/<slug:slug>',views.JoinGroup.as_view(),name='join'),
    path('leave/<slug:slug>',views.LeaveGroup.as_view(),name='leave')
]
