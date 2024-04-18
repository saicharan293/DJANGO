from django.shortcuts import get_object_or_404, render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data=Student.objects.all()
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


# def insertUpdateData(request,id):
    
    
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         age=request.POST.get('age')
#         gender=request.POST.get('gender')

#         if id:
#             # If student object exists, it's an update operation
#             student = Student.objects.get(pk=id)
#             student.name = name
#             student.email = email
#             student.age = age
#             student.gender = gender
#             student.save()
#             messages.info(request, "Data updated successfully")
#         else:
#             # If student object doesn't exist, it's an insertion operation
#             student = Student(name=name, email=email, age=age, gender=gender)
#             student.save()
#             messages.info(request, "Data inserted successfully")
        
#         return redirect('/')
#     return render(request,'index.html')

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