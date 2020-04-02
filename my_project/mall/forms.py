from django import forms

from mall.models import Product

class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['create_at', 'update_at']
        widgets = {
            # 修改表单的输入界面为单选按钮
            'types':forms.RadioSelect
        }

    def clean_price(self):
        """ 验证商品的价格 """
        price = self.cleaned_data['price']
        if int(price) < 0:
            raise forms.ValidationError('销售价格不能少于0')
        return price