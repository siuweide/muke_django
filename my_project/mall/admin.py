from django.contrib import admin


from mall.models import Product, Classify, Tag
from mall.forms import ProductAdminForm
from utils.admin_actions import set_invalid, set_valid


class ProductAdmin(admin.ModelAdmin):
    """ 商品信息管理 """
    list_display = ['name', 'types', 'price', 'status', 'is_valid']
    # 每页显示多少条数据
    list_per_page = 5
    list_filter = ['status']
    # 排除掉某些字段,使之不能编辑,在编辑页面不可见
    # exclude = ['ramain_count']
    # 不可编辑,但是在界面可以显示,只读
    readonly_fields = ['ramain_count']
    actions = [set_invalid, set_valid]
    # 添加字对应的表单
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)

@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    """ 商品分类管理 """
    list_display = ['name', 'parent', 'code', 'is_valid']


@admin.register(Tag)
class is_validAdmin(admin.ModelAdmin):
    """ 商品标签管理 """
    list_display = ('name', 'code', 'is_valid')
