from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'signin$', views.login_method, name='login'),
    url(r'signup$', views.register, name='register'),
    url(r'logout$', views.logout_method, name='logout'),
    url(r'kolbform$', views.kolb_form, name='kolb'),
    url(r'building$', views.building, name='building'),
    url(r'user/(?P<client_id>\d+)/profile$', views.user_profile, name='profile'),
]
