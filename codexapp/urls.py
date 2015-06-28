from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codexapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'lists/$', 'codexapp.main.views.lists', name='lists'),
    url(r'lists/add/$', 'codexapp.main.views.list_add', name='list_add'),
    url(r'lists/(\d*)/edit/$', 'codexapp.main.views.list_edit', name='list_edit'),

    url(r'lists/(\d*)/$', 'codexapp.main.views.list_view', name='list_view'),
    url(r'lists/(\d*)/prompts/(\d*)/$', 'codexapp.main.views.prompt_view', name='prompt_view'),
    url(r'lists/(\d*)/prompts/add/$', 'codexapp.main.views.prompt_add', name='prompt_add'),
    url(r'lists/(\d*)/prompts/(\d*)/send/$', 'codexapp.main.views.prompt_send', name='prompt_send'),

    url(r'people/(\d*)$', 'codexapp.main.views.user_view', name='user_view'),

    url(r'register/$', 'codexapp.main.views.register', name='register'),
    url(r'login/$', 'codexapp.main.views.login', name='login'),
    url(r'logout/$', 'codexapp.main.views.logout', name='logout'),

    url(r'profile/$', 'codexapp.main.views.profile', name='profile'),

    url(r'^$', 'codexapp.main.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
