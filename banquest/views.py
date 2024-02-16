from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, from index!")

def home(request):
    return HttpResponse("Hello, from home!")