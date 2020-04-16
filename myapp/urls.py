from django.urls import path,re_path

from django.contrib.auth import views as auth_views
from . import views
app_name = 'myapp'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('sign/',views.signin,name="sign"),
    path('refer/',views.refer_fun,name="refer"),
    path("ranklist/",views.ranklist,name="ranklist"),
    path('sendmail/',views.sendmail,name="sendmail"),
    re_path(r'^register/(?P<refer_code>[\w\-]+)/$',views.register,name="register"),
]
