"""ladynerds URL Configuration

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
from .views import contact, index, login, ladynerds, profile, resources, twitter_feed, code_of_conduct, faq, open_source,success
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^success/', success, name='success'),
    url(r'^contact/', contact, name='contact'),
    url(r'^login/', 'django.contrib.auth.views.login', name='foo',kwargs={'template_name': 'login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': index}),
    url(r'^ladynerds/', ladynerds, name='ladynerds'),
    url(r'^profile/', profile, name='profile'),
    url(r'^resources/', resources, name='resources'),
    url(r'^twitter_feed/', twitter_feed, name='twitter_feed'),
    url(r'^open_source/', open_source, name='open_source'),
    url(r'^code_of_conduct/', code_of_conduct, name='code_of_conduct'),
    url(r'^faq/', faq, name='faq')
]
