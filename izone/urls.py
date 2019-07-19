"""DevOps URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page
from django.conf import settings

from Precord.feeds import AllRecordOfSupportproblemRssFeed


urlpatterns = [
    url(r'',include('Precord.urls')),
    url(r'accounts/',include('users.urls')),
    url(r'Precord/',include('Precord.urls',namespace='Precord')),
    url(r'comment/',include('comment.urls',namespace='comment')),
    url(r'InstallRTOS/',include('InstallRTOS.urls',namespace='InstallRTOS')),
    url(r'T_map/',include('T_map.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^feed/$', AllRecordOfSupportproblemRssFeed(), name='rss'),
#    url(r'^sitemap\.xml$',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
#    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',    {'document_root': 'media'}),
]
if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
