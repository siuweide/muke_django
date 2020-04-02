import xadmin

from mall.models import Product

class ProductAdmin():
    """ 商品信息 """
    list_display = ['name', 'types', 'price', 'status', 'is_valid']
    list_filter = ['types', 'status']
    search_fields = ['name']

xadmin.site.register(Product, ProductAdmin)