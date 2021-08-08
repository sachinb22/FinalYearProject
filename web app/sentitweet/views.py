from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
	if request.method == 'POST':
	   	username = request.POST['username']
	   	password = request.POST['password']

	   	# user = User.objects.create_user(username=username,password=password)
	   	# user.save()
	   	user1 =auth.authenticate(username=username, password=password)
	   	if user1 is not None:
	   	  auth.login(request,user1)
	   	  return redirect('dashboard')  
	   	else:
	   		return redirect('login')
	else:
	  return render(request, 'accounts/login.html')

def logout(request):
	return redirect('index')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')