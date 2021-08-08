from django.urls import path
from .import views

urlpatterns = [
	path('configure',views.configure,name='configure'),
	path('analysis',views.analysis,name='analysis'),
	path('history',views.history,name='history'),
	
]