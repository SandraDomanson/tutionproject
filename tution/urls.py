"""tution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('login_page', views.login_page, name='login_page'),
    path('login', views.login, name='login'),
    path('homeadmin', views.homeadmin, name='homeadmin'),
    path('hometutor', views.hometutor, name='hometutor'),
    path('homestudent', views.homestudent, name='homestudent'),
    path('newtutor', views.newtutor, name='newtutor'),
    path('newstudent', views.newstudent, name='newstudent'),
    path('createtutor', views.createtutor, name='createtutor'),
    path('createstudent', views.createstudent, name='createstudent'),
    path('showtutor', views.showtutor, name='showtutor'),
    path('showstudent', views.showstudent, name='showstudent'),
    
    
    # re_path(r'^profileadmin/$',views.profileadmin, name='profileadmin'),
    # re_path(r'^profiletutor/$',views.profiletutor, name='profiletutor'),
    # re_path(r'^profilestudent/$',views.profilestudent, name='profilestudent'),
    
    
    path('tutlogin_page', views.tutlogin_page, name='tutlogin_page'),
    path('tutlogin', views.tutlogin, name='tutlogin'),
    path('stulogin_page', views.stulogin_page, name='stulogin_page'),
    path('stulogin', views.stulogin, name='stulogin'),
    
    
    # re_path(r'^resetpassword$', views.resetpassword, name='resetpassword'),
    # re_path(r'^passupdate/(?P<id>\d+)$', views.passupdate, name='passupdate'),
    

    path('shownotest', views.shownotest, name='shownotest'),
    path('shownotess', views.shownotess, name='shownotess'),
    path('maths', views.maths, name='maths'),
    path('chem', views.chem, name='chem'),
    path('social', views.social, name='social'),
    path('biology', views.biology, name='biology'),
    path('computer', views.computer, name='computer'),
    path('physics', views.physics, name='physics'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('logout', views.logout, name='logout')
]
