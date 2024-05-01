from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings_app.models import Meeting

# Create your views here.
def welcome(request):
    # return HttpResponse("<h2>welcome to Meeting Planner</h2>")
    context={
        'num_meetings':Meeting.objects.count(),
        'meetings':Meeting.objects.all(),
    }
    return render(request,'website/welcome.html',context)

def date(request):
    return HttpResponse("This page is serverd at "+str(datetime.now()))