#from django.http import HttpResponse
from django.shortcuts import render
import time
import datetime


def hello(request):
	context={}
	mt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	context['hello']=mt
	return render(request, 'hello.html', context)
