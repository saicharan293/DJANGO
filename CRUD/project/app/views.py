from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.
def index(request):
    query = request.GET.get('q')
    sort_column = request.GET.get('sort')
    sort_order = request.GET.get('order', 'asc')
    if query:
        # q=request.GET['q']
        data=Student.objects.filter(Q(name__icontains=query))
    else:
        data=Student.objects.all()

    if sort_column:
        if sort_order == 'asc':
            data = data.order_by(sort_column)
        else:
            data = data.order_by('-' + sort_column)
    page=request.GET.get('page',1)
    paginator=Paginator(data,3)
    try:
        data=paginator.page(page)
    except PageNotAnInteger:
        data=paginator.page(1)
    except EmptyPage:
        data=paginator.page(paginator.num_pages)

    content={'data':data}
    return render(request,'index.html',content)

def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data inserted successfully")
        return redirect('/')
    return render(request,'index.html')



def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data updated successfully")
        print("edit data",edit.name,edit.email,edit.age,edit.gender)
        return redirect("/")
    d=Student.objects.get(id=id)
    context={'d':d}
    return render(request,'edit.html',context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data deleted successfully")

    return redirect('/')