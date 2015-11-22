from django.template import Context
from django.core.mail import send_mail
from django.http import HttpResponse
import datetime
import urllib2
import json
from django.db.models import Count
from django.shortcuts import render_to_response 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from models import UploadFileForm
def index(request):
	email = ""
	password=""
	errors = []
	user_info = {}
	if request.user.is_authenticated():
		if request.user:
			user_info["name"] = request.user 
		else:
			user_info["name"] = "hao"
		return render_to_response('app2/index.html',{'errors': errors,"user_info":user_info,"flag_login":1})

	user= None
	flag_login = 0
	if request.method == 'POST':
		email = request.POST.get('email', '')
		password = request.POST.get('password', '')
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				user_info["name"] = email
				login(request, user)
				flag_login = 1
			else:
				errors.append("Not a active user")
		else:
			errors.append("Email or Password wrong")

	return render_to_response('app2/index.html',{'errors': errors,"user_info":user_info,"flag_login":flag_login})
def upload_page(request):
	email = ""
	password=""
	errors = []
	user_info = {}
	if request.user.is_authenticated():
		if request.user:
			user_info["name"] = request.user 
		else:
			user_info["name"] = "hao"
		return render_to_response('app2/upload.html',{'errors': errors,"user_info":user_info,"flag_login":1})
	return render_to_response('app2/upload.html')



def handle_uploaded_file(f):
	destination = open('/home/jasonhao/howspage.com/public/media/files/111', 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()


@login_required(login_url='/job/')
def upload_file(request):
	
  	if request.method == 'POST':
  		form = UploadFileForm(request.POST, request.FILES)
	# if form.is_valid():
		handle_uploaded_file(request.FILES['file'])
		return index(request)
	else:
		form = UploadFileForm()
		return HttpResponse('not valid')
	return render_to_response('app2/upload.html', {'form': form})



