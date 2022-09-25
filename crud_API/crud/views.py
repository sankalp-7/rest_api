from functools import partial
from urllib import response
from django.shortcuts import render,redirect
from.forms import UserForm
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from rest_framework.response import Response
from.serializers import crudserializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
# Create your views here.
#CRUD UI VIEWS BEGIN
def home(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request,'crud/index.html',{'form':form})
# class FormView(CreateView):
#     model=User
#     fields="__all__"
#     success_url="/student/"
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authlogin(request,user)
            return redirect('/view')
    return render(request,'crud/login.html')
def view(request):
    obj=User.objects.all()
    return render(request,'crud/User_list.html',{'obj':obj})
def Update(request,pk):
    obj=User.objects.get(id=pk)
    context={}
    form=UserForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/view')
    context["form"] = form
 
    return render(request, "crud/update.html", context)
def Delete(request,pk):
    obj=User.objects.get(id=pk)
    obj.delete()
    return redirect('/view')
#API VIEWS BEGIN
@api_view(['POST'])
def api_create(request):
    serializer=crudserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def api_delete(request,pk):
    event=User.objects.get(id=pk)
    event.delete()
    return Response('Deleted')
@api_view(['POST'])
def api_update(request,pk):
    event=User.objects.get(id=pk)
    serializer=crudserializer(instance=event,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def api_list(request):
    events=User.objects.all()
    serializer=crudserializer(events,many=True)
    return Response(serializer.data)
