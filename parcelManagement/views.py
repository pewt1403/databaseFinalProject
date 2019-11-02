from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
	header_str = 'Use template file'
	tableContent = 
	template = loader.get_template('parcelmanage.html')
	context = {
		'var1' : header_str
		'tc' : 
	}
	return HttpResponse(template.render(context,request))