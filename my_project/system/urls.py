from django.urls import path
from . import views

app_name='system'
urlpatterns = [
    # 新闻列表
    path('news/', views.news_list, name='news_list'),
    # 新闻详情
    path('new/<int:pk>/', views.news_detail, name='news_detail'),
    # 验证码
    path('verify/code/', views.verify_code, name='verify_code')
]