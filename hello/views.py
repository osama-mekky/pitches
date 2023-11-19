from django.shortcuts import render , redirect
from django.http import HttpResponse
from pitches .models import Pitche
# Create your views here.

def index(request):
    pitche = Pitche.objects.all()[0:3]


    return render(request,"index.html", {'pitche':pitche})