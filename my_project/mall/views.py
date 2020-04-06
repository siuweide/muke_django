from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from accounts.models import UserAddress
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
    # 用户的默认地址
    user = request.user
    default_addr = None
    if user.is_authenticated:
        default_addr = user.default_addr
        print('default_addr------>', default_addr)
    return render(request, 'prod_detail.html', {
        'prod_obj':prod_obj,
        'default_addr':default_addr
    })

class ProductList(ListView):
    """ 商品列表 """
    # 每页放多少条数据
    paginate_by = 6
    # 模板位置
    template_name = 'prod_list.html'

    def get_queryset(self):
        query = Q(status=constants.PRODUCT_STATUS_SELL, is_valid=True)
        # 按名称搜索
        name = self.request.GET.get('name', '')
        if name:
            query = query & Q(name__icontains=name)

        # 按标签进行搜索
        tag = self.request.GET.get('tag', '')
        if tag:
            query = query & Q(tags__code=tag)

        # 按照分类进行搜索
        cls = self.request.GET.get('cls', '')
        if cls:
            query =query & Q(classes__code=cls)
        return Product.objects.filter(query)

    def get_context_data(self, **kwargs):
        """ 添加额外的参数，添加搜索的参数 """
        context = super(ProductList, self).get_context_data(**kwargs)
        # context['search_name'] = self.request.GET.get('name', '')
        context['search_data'] = self.request.GET.dict()
        context['params'] = self.request.GET.dict()
        return context

def product_classify(request):
    """ 商品分类 """
    return render(request, 'prod_classify.html', {

    })