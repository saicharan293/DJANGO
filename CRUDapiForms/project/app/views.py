from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .serializers import StudentSerializer
from django.contrib import messages
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
@api_view(['GET','POST'])
def add_show(request):
    if request.method=='GET':
        fm = StudentRegistration()
        stud = Student.objects.all()
        paginator = Paginator(stud, 3) 
        page_number = request.GET.get('page')
        try:
            students = paginator.page(page_number)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)
        return render(request, 'show.html', {'form': fm, 'stu': students})
    elif request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            stud = Student.objects.all()
            paginator = Paginator(stud, 3)
            page_number = request.GET.get('page')
            try:
                students = paginator.page(page_number)
            except PageNotAnInteger:
                students = paginator.page(1)
            except EmptyPage:
                students = paginator.page(paginator.num_pages)
            return render(request, 'show.html', {'form': fm, 'stu': students})
    


@api_view(['GET', 'POST'])
def updateData(request,id):
    pi=Student.objects.get(pk=id)
    if request.method=="GET":
        fm=StudentRegistration(instance=pi)
        return render(request, 'edit.html', {'form': fm})
    elif request.method == "POST":
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    return render(request, 'edit.html', {'form': fm})
       
        



@api_view(['DELETE'])
def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('/')