from django.urls import path,include
from .views import AdminRegisterView,UserRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView
from .import views
urlpatterns = [

    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('userregister/',UserRegisterView.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('home/', views.home,name='home'),
    path('base/',views.base,name='base'),
    path('admin/dashboard/',views.AdminDashboardView.as_view(),name='admin_dashboard'),
    # path('user/dashboard/',views.UserDashBoardView.as_view(),name='user_dashboard'),
    path('nav/',views.base1,name='base'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
] 
