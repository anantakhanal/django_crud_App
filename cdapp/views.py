from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html")


def show(request):
    data = Entry.objects.all()
    return render(request, "show.html", {'data': data})


def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Name = request.POST['name']
        Data1 = request.POST['data1']
        Data2 = request.POST['data2']
        Entry(ID=ID, Name=Name, data1=Data1, data2=Data2).save()
        msg = "Data Stored Sucessfully"
        return render(request, "home.html", {'msg': msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")


def edit(request):
    ID = request.GET['id']
    data1= data2 = Name ="Not_Avilable"
    for data in Entry.objects.filter(ID=ID):
        Name =  data.Name
        data1 = data.data1
        data2 = data.data2

    return render(request, "edit.html", {'ID':ID,'Name':Name,'data1':data1,'data2':data2})

def RecordEdited(request):
    if request.method =='POST':
        ID = request.POST['id']
        Name= request.POST['name']
        data1= request.POST['data1']
        data2= request.POST['data2']
        Entry.objects.filter(ID=ID).update(Name=Name, data1=data1,data2 =data2 )
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - not found </h1>")
