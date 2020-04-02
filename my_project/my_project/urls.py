"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.urls import path, include
from my_project import settings
import xadmin
from xadmin.plugins import xversion
xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^$', views.index, name='index'),
    # 系统模块
    path('system/', include('system.urls', namespace='system')),
    # 用户账户模块
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # 商品模块
    path('mall/', include('mall.urls', namespace='mall'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
