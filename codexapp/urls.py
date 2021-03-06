from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codexapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'lists/$', 'codexapp.main.views.lists', name='lists'),
    url(r'lists/add/$', 'codexapp.main.views.list_add', name='list_add'),
    url(r'lists/(\d*)/edit/$', 'codexapp.main.views.list_edit', name='list_edit'),
    url(r'lists/(\d*)/subscribe/$', 'codexapp.main.views.list_subscribe', name='list_subscribe'),
    url(r'lists/(\d*)/unsubscribe/$', 'codexapp.main.views.list_unsubscribe', name='list_unsubscribe'),

    url(r'lists/(\d*)/$', 'codexapp.main.views.list_view', name='list_view'),
    url(r'lists/(\d*)/prompts/(\d*)/$', 'codexapp.main.views.prompt_view', name='prompt_view'),
    url(r'lists/(\d*)/prompts/(\d*)/delete/$', 'codexapp.main.views.prompt_delete', name='prompt_delete'),
    url(r'lists/(\d*)/prompts/(\d*)/respond$', 'codexapp.main.views.prompt_respond'),
    url(r'lists/(\d*)/prompts/add/$', 'codexapp.main.views.prompt_add', name='prompt_add'),
    url(r'lists/(\d*)/prompts/(\d*)/send/$', 'codexapp.main.views.prompt_send', name='prompt_send'),

    url(r'prompts/add/$', 'codexapp.main.views.prompt_add_quick', name='prompt_add_quick'),

    url(r'users/(?P<username>[-\w]+)$', 'codexapp.main.views.user_view', name='user_view'),

    url(r'register/$', 'codexapp.main.views.register', name='register'),
    url(r'login/$', 'codexapp.main.views.login', name='login'),
    url(r'logout/$', 'codexapp.main.views.logout', name='logout'),

    url(r'profile/edit/$', 'codexapp.main.views.profile_edit', name='profile_edit'),

    url(r'api/prompt/(\d*)/$', 'codexapp.main.api.prompt', name='api_prompt'),
    url(r'api/reply/(\d*)/upvote/$', 'codexapp.main.api.reply_upvote', name='api_reply_upvote'),

    url(r'^$', 'codexapp.main.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # only works during debug mode
