from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from accounts.models import User, UserProfile, UserAddress, LoginRecord


class UserAdmin(UserAdmin):
    """ 用户基础信息 """
    list_display = ['format_username', 'nickname', 'integral', 'is_active']
    # 支持用户名、昵称搜索
    search_fields = ['username', 'nickname']
    # 添加自定义的方法
    actions = ['disable_user', 'enable_user']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'integral', 'nickname', 'level')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def format_username(self, obj):
        """ 用户名脱敏处理 """
        return obj.username[0:3] + '***'

    # 修改列名显示
    format_username.short_description = '用户名'

    def disable_user(self, request, queryset):
        """ 批量禁用选中的用户 """
        queryset.update(is_active=False)
    disable_user.short_description = '批量禁用选中的用户'

    def enable_user(self, request, queryset):
        """ 批量禁用选中的用户 """
        queryset.update(is_active=True)
    enable_user.short_description = '批量启用选中的用户'

admin.site.register(User,UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """ 用户详细信息 """
    list_display = ('user', 'phone_no', 'sex')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    """ 用户地址管理 """
    list_display = ('user', 'province', 'city',
                    'username', 'address', 'phone')
    search_fields = ('user__username', 'user__nickname',
                     'phone')

@admin.register(LoginRecord)
class LoginRecordAdmin(admin.ModelAdmin):
    """ 登录历史记录 """
    list_display = ['username', 'ip', 'address', 'source']