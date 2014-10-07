from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # URL:
    url(r'^$', 'loflee.views.home', name='home'),
    url(r'^profile/$', 'loflee.views.profile', name='profile'),
    url(r'^seeprofiles/$', 'loflee.views.seeprofiles', name='seeprofiles'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^seeprofile/(?P<user_id>\w+)/$', 'loflee.views.seeprofile', name='seeprofile'),
    url(r'^chat/(?P<sender>\w+)/(?P<receiver>\w+)/$', 'loflee.views.chat', name='chat'),
    url(r'^about/$', 'loflee.views.about', name='about'),
    url(r'^contact/$', 'loflee.views.contact', name='contact'),




        #LOGIN AND REGISTER
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'loflee.views.register', name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # PASSWORD RESET
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)