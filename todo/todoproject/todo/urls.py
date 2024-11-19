from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),  
    path('login/', views.admin_login, name='admin_login'),
    path('panel/', views.admin_panel, name='admin_panel'),
    path('member/login/', views.member_login, name='member_login'),
    path('member/panel/', views.member_panel, name='member_panel'),  # Üye paneli
    path('user/tasks/', views.user_tasks, name='user_tasks'),
    path('tasks/', views.admin_view_tasks, name='admin_view_tasks'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
