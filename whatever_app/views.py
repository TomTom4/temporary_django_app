from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
	return HttpResponse("This is the app, it is working now at : {0}".format(datetime.datetime.now()))
