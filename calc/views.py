from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return "Hello, world"
    
    #we need to give output in a response format so we use http
    #return HttpResponse("Hello world")
    
    #return render(request,'home.html')

    #for dynamic :
    return render(request, 'home.html', {'name':'Anou'})


def add(request):

    #fetch values from form
    val1=int(request.POST['n1'])
    val2=int(request.POST['n2'])
    res=val1+val2

    return render(request,'result.html',{'result':res})