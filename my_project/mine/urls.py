from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'mine'
urlpatterns = [
    # 订单详情
    path('order/detail/<str:sn>/', login_required(views.OrderDetailView.as_view()), name='order_detail'),
    # 添加购物车
    path('cart/add/<int:cid>/', views.cart_add, name='cart_add'),
    # 我的购物车
    path('cart/', views.cart, name='cart'),
    # 提交订单
    path('order/pay/', views.order_pay, name='order_pay')
]