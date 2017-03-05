from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'stud_assess/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^marks/(?P<stud_id>[0-9].*)$', views.displayMarks, name='marks')
]
