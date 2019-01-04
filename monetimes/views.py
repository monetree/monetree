from django.http import HttpResponse


def handler_404(request):
    return HttpResponse("404")

def handler_500(request):
    return HttpResponse("500")

def handler_403(request):
    return HttpResponse("403")

def handler_400(request):
    return HttpResponse("400")
