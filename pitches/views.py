from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q

from django.core.paginator import Paginator

def pitches(request):
    q=''

    if request.GET.get('q') != None :
         q= request.GET.get('q')
    else :
         ''     
    pitche = Pitche.objects.filter(Q(city__name__icontains=q)|Q(Name__icontains = q))
    pitche_count=pitche.count()
    
    #paginations
    #pitt = Pitche.objects.all()
    paginator = Paginator(pitche,12)
    page = request.GET.get('page')
    paged_pitches = paginator.get_page(page)

    context ={
        #'pitche':pitche,
        'citys' :City.objects.all(),
        'pitche_count':pitche_count,
        'paged_pitches':paged_pitches,   

    }
    return render(request,'pitches/pitches.html',context)






def pitche_page(request,id):

    if request.method == 'POST' and request.user.is_authenticated :
            instance = OpeningHours(pitche_id=id, user=request.user)
            add_date = RestaurantForm(request.POST, request.FILES, instance=instance)
            if add_date.is_valid():
                # الحجز على رأس الساعة 
                minn_from = instance.from_hour.minute > 0
                minn_to = instance.to_hour.minute > 0
                #########################################

                # الحجز لمدة اقل من ساعة او اكثر من 4 ساعات 
                x= instance.to_hour -instance.from_hour
                if instance.from_hour >= instance.to_hour :
                     messages.error(request,"خطأ في إدخال التوقيت")
                elif instance.from_hour <=timezone.now():
                     messages.error(request,"هذا التوقيت قد فات")     
                elif minn_from or minn_to :
                     messages.error(request,'لا يمكن الحجز الا من بداية الساعة ')
                elif x >= datetime.timedelta(1) or x > datetime.timedelta(0,00,00,00,00,4):
                     messages.error(request,'لا يمكن الحجز اكثر من 4 ساعات ')           
                else:     

                    add_date.save()
                    messages.success(request, "تم الحجز بنجاح")
            else:
                messages.error(request, 'هذا التوقيت محجوز مسبقا') 
    
    context ={
        'pit':get_object_or_404(Pitche,id=id),
        'form':RestaurantForm(),
    }
    return render(request,'pitches/pitche.html',context)



def delateBooking(request,id):
     booking = OpeningHours.objects.get(id=id)
     if booking.user.id == request.user.id:
            booking.delete()  
    #  if request.method == 'POST':
    #     booking.delete()
     return redirect('profile')








   
    





