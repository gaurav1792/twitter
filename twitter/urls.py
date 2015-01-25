from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'twitter_app.views.index'),
    url(r'^login$', 'twitter_app.views.login_view'),
    url(r'^logout$', 'twitter_app.views.logout_view'),
    url(r'^signup$', 'twitter_app.views.signup'),
    url(r'^submit$', 'twitter_app.views.submit'),
    url(r'^users/$', 'twitter_app.views.users'),
	url(r'^following/$', 'twitter_app.views.following'),
	url(r'^following/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', 'twitter_app.views.following'),
    url(r'^users/(?P<username>\w{0,50})/$', 'twitter_app.views.users'),
	url(r'^users/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', 'twitter_app.views.users'),
    url(r'^follow$', 'twitter_app.views.follow'),
	url(r'^unfollow$', 'twitter_app.views.unfollow'),
	url(r'^retweet$', 'twitter_app.views.retweet'),
)
