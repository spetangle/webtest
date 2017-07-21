from django.http import HttpResponse
from django.shortcuts import render
import random
import time
import datetime


def index(request):
	context={"pageTitle":"haha !","pageHeader":"121212"}
	return render(request, 'index.html', context)


def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))


def add1(request,a, b):
    context={"result":int(a)+int(b)}
    context["num1"] = int(random.random()*100)
    context["num2"] = int(random.random() * 100)
    return render(request, 'hello.html', context)