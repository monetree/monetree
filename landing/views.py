from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def landing(request):
    return render(request,'index.html',{})


def error_404(request):
    return render(request,'error.html')

def error_500(request):
    return render(request,'error.html')

def error_404_demo(request):
    return render(request,'error.html')

def error_500_demo(request):
    return render(request,'error.html')
