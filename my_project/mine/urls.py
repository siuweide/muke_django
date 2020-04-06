from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import OrderListView

app_name = 'mine'
urlpatterns = [
    # 个人中心
    path('', views.index, name='index'),
    # 订单详情
    path('order/detail/<str:sn>/', login_required(views.OrderDetailView.as_view()), name='order_detail'),
    # 添加购物车
    path('cart/add/<int:cid>/', views.cart_add, name='cart_add'),
    # 我的购物车
    path('cart/', views.cart, name='cart'),
    # 提交订单
    path('order/pay/', views.order_pay, name='order_pay'),
    # 我的订单
    path('order/list/', views.login_required(OrderListView.as_view()), name='order_list'),
    # 我的收藏
    path('prod/collect/', views.prod_collect, name='prod_collect'),
]