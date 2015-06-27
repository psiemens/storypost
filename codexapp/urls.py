from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codexapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'lists/$', 'codexapp.main.views.lists', name='lists'),
    url(r'lists/add/$', 'codexapp.main.views.list_add', name='list_add'),
    url(r'lists/(\d*)/edit/$', 'codexapp.main.views.list_edit', name='list_edit'),

    url(r'prompts/$', 'codexapp.main.views.prompts', name='prompts'),
    url(r'prompts/add/$', 'codexapp.main.views.prompt_add', name='prompt_add'),
    url(r'prompts/(\d*)/edit/$', 'codexapp.main.views.prompt_edit', name='prompt_edit'),

    url(r'/', 'codexapp.main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
