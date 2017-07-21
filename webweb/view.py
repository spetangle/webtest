#from django.http import HttpResponse
from django.shortcuts import render
import time
import datetime

def hello(request):
	now =datetime.datetime.now()
	context={}
	context['hello']=str(now.strtime('%c‘))
	return render(request, 'hello.html', context)
