from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """ 用户的基础信息表 """
    # username = models.CharField('用户名', max_length=64)
    # password = models.CharField('密码', max_length=255)
    avatar = models.ImageField('用户头像', upload_to='avatar', null=True)
    integral = models.IntegerField('用户积分', default=0)
    nickname = models.CharField('昵称', max_length=32)
    level = models.SmallIntegerField('用户级别')

    class Meta:
        db_table = 'accounts_user'
        verbose_name = '用户基础信息'
        verbose_name_plural = '用户基础信息'

class UserProfile(models.Model):
    """ 用户的详细信息 """
    SEX_CHOICES = (
        (1, '男'),
        (0, '女'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    real_name = models.CharField('真实姓名', max_length=32)
    email = models.CharField('电子邮箱', max_length=128, null=True, blank=True)
    is_email_valid = models.BooleanField('邮箱是否已经验证', default=False)
    phone_no = models.CharField('手机号码', max_length=20, null=True, blank=True)
    is_phone_valid = models.BooleanField('手机号码是否已经验证', default=False)
    sex = models.SmallIntegerField('性别', default=1, choices=SEX_CHOICES)
    age = models.SmallIntegerField('年龄', default=0)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'accounts_user_profile'
        verbose_name = '用户详细信息'
        verbose_name_plural = '用户详细信息'


class UserAddress(models.Model):
    """ 用户地址信息 """
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    province = models.CharField('省份', max_length=32)
    city = models.CharField('市区', max_length=32)
    area = models.CharField('区域', max_length=32)
    town = models.CharField('街道', max_length=32, null=True, blank=True)

    address = models.CharField('详细地址', max_length=64)
    username = models.CharField('收件人', max_length=32)
    phone = models.CharField('收件人的电话', max_length=32)

    is_default = models.BooleanField('是否为默认地址', default=False)
    is_valid = models.BooleanField('是否有效', default=True)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'accounts_user_address'
        ordering = ['is_default', '-updated_at']
        verbose_name = '用户地址信息'
        verbose_name_plural = '用户地址信息'

    def get_phone_format(self):
        """ 手机号码格式化 """
        return self.phone[0:3] + '****' + self.phone[6:-1]

    def get_region_format(self):
        """ 省市区 """
        return '{self.province} {self.city} {self.area}'.format(self=self)

class LoginRecord(models.Model):
    """ 用户的登录历史 """
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField('登录的账号', max_length=64)
    ip = models.CharField('IP', max_length=32, null=True, blank=True)
    address = models.CharField('地址', max_length=32)
    source = models.CharField('登录的来源', max_length=32)

    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'accounts_login_record'
        verbose_name = '登录历史记录'
        verbose_name_plural = '登录历史记录'
