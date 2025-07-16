from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('explore/', views.explore, name='explore'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('messages/', views.messages, name='messages'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_detail/', views.post_detail, name='post_detail'),
    path('find_friends/', views.find_friends, name='find_friends'),
    path('friend_requests/', views.friend_requests, name='friend_requests'),
    path('notifications/', views.notifications, name='notifications'),
    path('saved/', views.saved, name='saved'),
    path('invite/', views.invite, name='invite'),
    path('setting/', views.setting, name='setting'),
]
