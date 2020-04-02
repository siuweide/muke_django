from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from mall.models import Product
from utils import constants

def product_list(request):
    """ 商品列表 """
    prod_list = Product.objects.filter(status=constants.PRODUCT_STATUS_SELL, is_valid=True)
    name = request.GET.get('name', '')
    prod_list = prod_list.filter(name__icontains=name)
    return render(request, 'prod_list.html', {
        'prod_list':prod_list
    })


def product_detail(request, pk):
    """ 商品详情 """
    prod_obj = get_object_or_404(Product, id=pk, is_valid=True)
    return render(request, 'prod_detail.html', {
        'prod_obj':prod_obj
    })

class ProductList(ListView):
    """ 商品列表 """
    # 每页放多少条数据
    paginate_by = 5
    # 模板位置
    template_name = 'product_list.html'

    def get_queryset(self):
        query = Q(status=constants.PRODUCT_STATUS_SELL, is_valid=True)
        # 按名称搜索
        name = self.request.GET.get('name', '')
        if name:
            query = query & Q(name__icontains=name)
        return Product.objects.filter(query)