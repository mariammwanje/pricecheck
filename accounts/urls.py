from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import LoginView, SignupView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),

]

urlpatterns += staticfiles_urlpatterns()
