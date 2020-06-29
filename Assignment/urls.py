from django.urls import path
from django.conf.urls import url
from Assignment import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Assignmnent', views.Assignment, name='Assignment'),
    path('Register', views.Register, name='Register'),
    path('Profile', views.ProfilePage, name='ProfilePage'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
    path('CheckUsernameUniqueness', views.CheckUsernameUniqueness, name='CheckUsernameUniqueness'),
    path('CheckPasswordCorrectness', views.CheckPasswordCorrectness, name='CheckPasswordCorrectness'),
    path('CheckEmailUniqueness', views.CheckEmailUniqueness, name='CheckEmailUniqueness'),
    path('EmailVerification', views.EmailVerification, name='EmailVerification'),
    path('PhoneVerification', views.PhoneVerification, name='PhoneVerification'),
    path('SendCodeEmail', views.SendCodeEmail, name='SendCodeEmail'),
    path('SendCodePhone', views.SendCodePhone, name='SendCodePhone'),
    path('ApplyVerifyEmail', views.ApplyVerifyEmail, name='ApplyVerifyEmail'),
    path('ApplyVerifyPhone', views.ApplyVerifyPhone, name='ApplyVerifyPhone'),
]
