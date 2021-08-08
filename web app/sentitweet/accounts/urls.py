from django.urls import path
from .import views

urlpatterns = [
	path('login',views.login,name='login'),
	path('userlog',views.userlog,name='userlog'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('logout',views.logout,name='logout')
 ]