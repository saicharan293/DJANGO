from django.http import HttpResponse
from django.shortcuts import render

# from genre.forms import UserForm
from genre.models import Collection, Piece
# from django.contrib.auth import authenticate,login
from django.views.generic import View

# Create your views here.
def index(request):
    all_collections=Collection.objects.all()
    # print("all collections",all_collections)
    context={
        "all_collections":all_collections
    }
    # print("context",context)
    return render(request,"genre.html",context)

def details(request,genre_id):
    Citem=Collection.objects.get(pk=genre_id)
    pitem=Piece.objects.filter(collection=Citem)
    context={
        "pitem":pitem
    }
    print("pitem",pitem)
    return render(request,"detail.html",context)


# def details(request,genre_id):
#     return HttpResponse("<h1>the genre id is: "+genre_id+"</h1>")
