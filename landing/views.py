from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def landing(request):
    return render(request,'index.html',{})
