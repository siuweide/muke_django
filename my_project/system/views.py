from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render

from system.models import News
# Create your views here.
from utils import constants
from utils.verify import VerifyCode


def news_list(request):
    page = request.GET.get('page', 1)
    page_size = 10
    news_objects = News.objects.filter(types=constants.NEWS_TYPE_NEW,
                                       is_valid=True).order_by('id')
    p = Paginator(news_objects, page_size)
    page_data = p.page(page)
    print(page_data)
    return render(request, 'news_list.html', {
        'page_data':page_data
    })


def news_detail(request,pk):
    """ 新闻详情 """
    detail = News.objects.get(id=pk, is_valid=True)
    detail.views_count = F('views_count') + 1
    detail.save()
    detail.refresh_from_db()
    return render(request, 'news_info.html', {
        'detail':detail
    })

def verify_code(request):
    client = VerifyCode(request)
    return client.gen_code()