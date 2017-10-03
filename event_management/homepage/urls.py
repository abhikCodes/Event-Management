from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^clubs/$', views.club, name='club'),
    url(r'^register/', views.register,name='register'),
    url(r'^login/$', auth_views.login,{'template_name':'homepage/login.html'}),
    url(r'^logout/$', auth_views.logout,{'template_name':'homepage/logout.html'}),
    
 ]
