"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.views.decorators.csrf import csrf_exempt

from main.models import Manufacturer, Cereal, NutritionFacts, DisplayShelf

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home'),
    url(r'^cereal_search/$', 'main.views.cereal_search'),
    url(r'^manufacturer_search/$', 'main.views.get_manufacturer_search'),
    url(r'^post_manufacturer_search/$', 'main.views.post_manufacturer_search'),
    url(r'^actual_post_manufacturer_search/$', 'main.views.actual_post_manufacturer_search'),
    url(r'^template_view_2/$', 'main.views.template_view_2'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^ajax/$','main.views.ajax'),
    url(r'^form_view/$','main.views.form_view'),
    url(r'^form_view2/$','main.views.form_view2'),
    url(r'^cereal_create/$','main.views.cereal_create'),
    #url(r'^template_view_ajax/$','main.views.template_view_ajax'),
    url(r'^signup/(?P<registrationpage>\d+)/$','main.views.signup'),
    url(r'^signup/$','main.views.signup'),
    url(r'^testing/$','main.views.testing'),
    url(r'^login/$','main.views.login_view'),
    url(r'^logout/$','main.views.logout_view'),
]
