from django.contrib import messages


def set_invalid(modelAdmin, request, queryset):
    """ 逻辑禁用is_valid=False """
    queryset.update(is_valid=False)
    messages.success(request, '操作成功')

set_invalid.short_description = '禁用所选对象'


def set_valid(modelAdmin, request, queryset):
    """ 逻辑启用is_valid=True """
    queryset.update(is_valid=True)
    messages.success(request, '操作成功')

set_valid.short_description = '启用所选对象'