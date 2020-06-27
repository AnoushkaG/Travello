from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dests=Destination.objects.all()
    # dest1=Destination()
    # dest1.name='Mumbai'
    # dest1.desc='Lolololo'
    # dest1.id=1
    # dest1.img='destination_1.jpg'
    # dest1.price=1000
    # dest1.offer=False

    # dest3=Destination()
    # dest3.name='toer'
    # dest3.desc='Lolololo'
    # dest3.id=1
    # dest3.img='destination_3.jpg'
    # dest3.price=1000
    # dest3.offer=True 
    
    # dest2=Destination()
    # dest2.name='pandarpur'
    # dest2.desc='Lolololo'
    # dest2.id=1
    # dest2.offer=False 
    # dest2.img='destination_2.jpg'
    # dest2.price=1000

 

    #dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})