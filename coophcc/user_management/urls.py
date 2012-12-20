from django.conf.urls.defaults import *

from django.contrib import auth

urlpatterns = patterns('',
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
	(r'^password_change/$', 'django.contrib.auth.views.password_change'),
	(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),
	(r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
	(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
	(r'^password_reset_confirm/$', 'django.contrib.auth.views.password_reset_confirm'),
	(r'^password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete'),
	(r'^create_account/$', 'user_management.views.create_account'),
	(r'^edit_profile/$', 'user_management.views.edit_profile'),
	(r'^profile/$', 'user_management.views.profile'),
	(r'^$', 'user_management.views.profile'),
)