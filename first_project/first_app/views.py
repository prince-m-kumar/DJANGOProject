from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World")

def index(request):
    my_dirt = {'insert_me':"Hello i comming from first app"}
    return render(request,'first_app\index.html',context=my_dirt)
