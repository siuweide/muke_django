from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 用户登录
    path("user/login/", views.user_login, name='user_login'),
    # 用户退出
    path("user/logout/", views.user_logout, name='user_logout'),
    # 用户注册
    path('user/register/', views.user_register, name='user_register'),
    # 用户地址
    path('user/address/list/', views.address_list, name='address_list'),
    # 新增地址
    path('user/address/add/', views.address_add, name='address_add'),
    # 编辑地址
    path('user/address/edit/<int:pk>/', views.address_edit, name='address_edit'),
    # 删除地址
    path('user/address/delete/<int:pk>/', views.address_delete, name='address_delete')
]