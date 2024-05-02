from django.shortcuts import render,get_object_or_404,redirect
from meetings_app.models import Meeting,Room

from .forms import MeetingForm
# Create your views here.
def meeting_details_view(request,id):
    m_id=get_object_or_404(Meeting,pk=id)
    context={
        'title':m_id.title,
        'date':m_id.date,
        'start_time':m_id.start_time,
        'room':m_id.room
    }
    return render(request,'meetings/detail.html',context)

def rooms_view(request):
    rooms=Room.objects.all()
    context={
        'rooms':rooms
    }
    return render(request,'meetings/rooms_list.html',context)


# MeetingForm=modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=MeetingForm()
    return render(request,'meetings/new.html',{'form':form})