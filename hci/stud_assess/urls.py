from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login$', auth_views.login, name='teacher_login'),
    # url(r'^logout$', auth_views.logout, name='logout'),

    url('^', include('django.contrib.auth.urls')),

    # Using parentheses around a pattern 'captures' the text matched by that pattern and
    # sends it as an argument to the view function;
    # ?P<question_id> defines the name that will be used to identify the matched pattern;
    # and [0-9]+ is a regular expression to match a sequence of digits (i.e., a number).
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]
