from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
import re
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from pitches.models import OpeningHours ,Manager

from django.utils import timezone
import datetime 


# Create your views here.

def Register(request):
        #عمل هنا تححق علشان لو المستخدم عمل تسجيل دخول بالفعل ميقدرش يشوف صفحة تسجيل الدخول تاني 
    if request.user.is_authenticated:
        return redirect('index')
    else :
        if request.method == 'POST':
            fname = request.POST['fName']
            lName = request.POST['lName']
            age = request.POST['age']
            phone_number = request.POST['phone_number']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            conf_password = request.POST['conf_password']

            if User.objects.filter(username=username).exists():
                messages.error(request,'اسم المستخدم موجود مسبقا')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'البريد الألكتروني موجود مسبقا')
                else :
                    patt= "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                    patt_number = r"\d{11}"
                    patt_age = r"\d{2}"
                    if re.match(patt_age,age):
                        if re.match(patt_number,phone_number):

                            if re.match(patt,email):
                                if re.match(password,conf_password):
                                    user = User.objects.create_user(first_name = fname,last_name = lName,email=email,username=username,password=password)
                                    user.save()
                                    userprofile = UserProfile(user=user,age=age,phone_number=phone_number)
                                    userprofile.save()
                                    messages.success(request,'تم انشاء الحساب بنجاح')
                                    
                                    
                                else:
                                    messages.error(request,"كلمة السر غير متطابقة")

                            else :
                                messages.error(request,"خطأ في البريد الألكتروني")
                        else :
                            messages.error(request,"خطأ في رقم الهاتف")
                    else : 
                        messages.error(request,"خطأ في العمر")






    return render(request,'accounts/Register.html') 

def Login(request):
    #عمل هنا تححق علشان لو المستخدم عمل تسجيل دخول بالفعل ميقدرش يشوف صفحة تسجيل الدخول تاني 
    if request.user.is_authenticated:
        return redirect('index')
    else :
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None :
                if 'rememberme' not in request.POST:
                    request.session.set_expiry(0)
                auth.login(request,user)
                return redirect('index')
            else :
                messages.error(request,"Username Or Password is Invaild")



    return render(request,'accounts/Login.html') 

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')  

@login_required(login_url='login')
def profile(request):
    openingHours = OpeningHours.objects.all()
    manager = Manager.objects.all()
    time = timezone.now()
    # for i in openingHours :
    #       active= i.created +datetime.timedelta(minutes=2)
          

          
    
    if request.method=='POST' and 'btnsave' in request.POST:
        if request.user is not None and request.user.id != None :
            userprofile = UserProfile.objects.get(user = request.user)
            if request.POST['fname'] and request.POST['lname'] and request.POST['age'] and request.POST['phone_number'] and request.POST['username'] and request.POST['email'] and request.POST['password'] :
                request.user.first_name = request.POST['fname']
                request.user.last_name = request.POST['lname']
                userprofile.age = request.POST['age']
                userprofile.phone_number = request.POST['phone_number']
                if not request.POST['password'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['password'])
                request.user.save()
                userprofile.save()
                auth.login(request,request.user)    
        return redirect('profile')
    else :
        if request.user is not None :
            userprofile = UserProfile.objects.get(user=request.user)

            context ={
                'fname':request.user.first_name,
                'lname':request.user.last_name,
                'age':userprofile.age,
                'phone':userprofile.phone_number,
                'email':request.user.email,
                'user':request.user.username,
                'pass':request.user.password,
                'openingHours':openingHours,
                'time':time,
                'manager':manager,
                
                
                

            }
            return render(request,'accounts/profile.html',context)
        
