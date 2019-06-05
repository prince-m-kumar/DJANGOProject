from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,webPage,AccessRecord
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World")

def index(request):
    my_dirt = {'insert_me':"Hello i comming from first app"}
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,'first_app\index.html',context=date_dict)
