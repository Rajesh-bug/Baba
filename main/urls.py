from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newbaba', views.newbaba, name='newbaba'),
    path('newslip', views.newslip, name='newslip'),
    path('addgotra', views.addgotra, name='addgotra'),
    path('addvidhi', views.addvidhi, name='addvidhi'),
    path('login', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('navbar/', views.navbar, name='navbar'),
    path('signup', views.userCreate, name="signup"),
    path('invoice', views.invoice, name="invoice"),
]
