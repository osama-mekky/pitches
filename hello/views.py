from django.shortcuts import render , redirect
from django.http import HttpResponse
from pitches .models import Pitche 
from django.contrib import messages
from .models import Contact
# Create your views here.
import re

def index(request):
    pitche = Pitche.objects.all()[0:3]


    return render(request,"index.html", {'pitche':pitche})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        subject = request.POST['subject']
        meassage = request.POST['message']
        patt= "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
        patt_number = r"\d{11}"
        if re.match(patt,email):
            if re.match(patt_number,phone_number):
                mess = Contact.objects.create(name=name , email=email,phone_number=phone_number,subject=subject,message=meassage)
                mess.save()
                messages.success(request,'تم إرسال الرسالة بنجاح ')
            else :
                messages.error(request,'خطأ في إدخال رقم الهاتف')
        else :
            messages.error(request,' البريد الألكتروني غير صحيح')



    return render (request,'contact.html')

