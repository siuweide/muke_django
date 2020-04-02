from datetime import datetime
from django.shortcuts import render_to_response, render
from accounts.models import User
from system.models import Slider,News
from utils import constants
from utils import constants


def index(request):
    """ 首页 """
    # 查询轮播图
    slider_list = Slider.objects.filter(types=constants.SLIDER_TYPE_INDEX)
    # 首页的新闻
    now_time = datetime.now()
    # 置顶的，有效的，在时间范围内的
    news_list = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                                    is_top=True,
                                    is_valid=True,
                                    start_time__lte=now_time,
                                    end_time__gte=now_time)
    # 从Session中获取用户id
    # user_id = request.session[constants.LOGIN_SESSION_ID]
    # user = User.objects.get(pk=user_id)
    return render(request, 'index.html', {
        'slider_list':slider_list,
        'news_list':news_list,
        # 'user':user
    })