from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
# 	return HttpResponse("<em> My Second Project</em>")
#

def index(request):
	my_dirt = {'my_dirt':"Hello i comming from first app"}
	return render(request,'appTwo\help.html',context=my_dirt)
