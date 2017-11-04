"""from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^clubs/$', views.club, name='club'),
    url(r'^register/', views.register,name='register'),
    url(r'^login/$', auth_views.login,{'template_name':'homepage/login.html'}),
    url(r'^logout/$', auth_views.logout,{'template_name':'homepage/logout.html'}),
    url(r'^register/tag/$', views.tag,name='tag'),
    
 ]
"""
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^clubs/(?P<clubname>[A-Za-z]{2,20})/$', views.club, name='club'),
    url(r'^event/(?P<pk>\d+)/$', views.events_detail, name='events_detail'),
    url(r'^unauthenticated/', views.unauthentic,name='unauthentic'),
    url(r'^changepass/', views.ChangePass, name='ChangePass'),
    url(r'^register/', views.register,name='register'),
    url(r'^forgotpass/', views.ForgotPass, name='ForgotPass'),
    # url(r'^login/$', auth_views.login,{'template_name':'homepage/LoginPage.html'}),
    # url(r'^logout/$', auth_views.logout, {'template_name':'homepage/index.html'}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^login/', views.Login, name='Login'),
    url(r'^tag/$', views.tag,name='tag'),
    url(r'^sel_tag/$', views.sel_tag,name='sel_tag'),
    url(r'^club_admin/$', views.simple_upload, name='simple_upload'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^edittag/$', views.edit_tag, name='edit_tag'),
 ]