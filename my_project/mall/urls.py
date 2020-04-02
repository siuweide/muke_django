from django.urls import path
from . import views

app_name = 'mall'
urlpatterns = [
    # 商品列表
    path("prod/list/", views.product_list, name='product_list'),
    # 商品详情
    path("prod/detail/<int:pk>/", views.product_detail, name='product_detail')
]