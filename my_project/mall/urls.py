from django.urls import path
from . import views

app_name = 'mall'
urlpatterns = [
    # 商品列表 def function来实现
    # path("prod/list/", views.product_list, name='product_list'),
    # 使用class 来实现
    path("prod/list/", views.ProductList.as_view(), name='product_list'),
    # 加载HTML片段的地址
    path("prod/load/list/", views.ProductList.as_view(
        template_name = 'product_load_list.html'
    ), name='product_load_list'),
    # 商品详情
    path("prod/detail/<int:pk>/", views.product_detail, name='product_detail')
]