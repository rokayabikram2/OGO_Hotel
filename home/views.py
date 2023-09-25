from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from adminpanel.models import GlobalSettings,Contact,Navigation,Booking,Rooms_detail

# Create your views here.
# def base(request):
#   glob=GlobalSettings.objects.all()
  
#   return render(request,'base.html',{'glob':glob})

def home(request):
  glob=GlobalSettings.objects.all()
  sliders= Navigation.objects.filter(page_type="Home/Slider",status="Publish")
  abouts = Navigation.objects.filter(page_type="About",status="Publish")
  teams=Navigation.objects.filter(page_type="Our Team", status="Publish")
  testi =Navigation .objects.filter(page_type="Testimonial",status="Publish")
  serv = Navigation.objects.filter(page_type="Service", status="Publish")
  
  r_detail=Rooms_detail.objects.all()
  
  
  
  return render(request,'index.html',{'glob':glob,'sliders':sliders,'abouts':abouts,'teams':teams,'testi':testi,'serv':serv,'r_detail':r_detail})


def about(request):
  glob=GlobalSettings.objects.all()
  abouts = Navigation.objects.filter(page_type="About",status="Publish")
  teams=Navigation.objects.filter(page_type="Our Team", status="Publish")

  
  return render(request,'about.html',{'glob':glob,'abouts':abouts,'teams':teams})


def room(request):
  glob=GlobalSettings.objects.all()
  rooms = Navigation.objects.filter(page_type="Rooms",status="Publish")
  testi =Navigation .objects.filter(page_type="Testimonial",status="Publish")
  r_detail=Rooms_detail.objects.all()
  
  return render(request,'room.html',{'glob':glob,'testi':testi,'r_detail':r_detail,'rooms':rooms})

# def login(request):
#   glob=GlobalSettings.objects.all()
  
#   return render(request,'login.html',{'glob':glob})

def service(request):
  glob=GlobalSettings.objects.all()
  serv = Navigation.objects.filter(page_type="Service", status="Publish")
  testi =Navigation .objects.filter(page_type="Testimonial",status="Publish")
  
  
  
  return render(request,'service.html',{'glob':glob,'serv':serv,'testi':testi})

def booking(request):
  glob=GlobalSettings.objects.all()
  books= Navigation.objects.filter(page_type="Booking",status="Publish")
   
  if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        child = request.POST.get('child')
        adult = request.POST.get('adult')
        rooms = request.POST.get('rooms')
        checkin =request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        n_rooms = request.POST.get('n_rooms')
        
        
        # if len(name)<2 or len(email)<3 or len(subject)<4 or len(message)<2:
        #     messages.error(request,"Cannot submit your message. Something went wrong.")

        # else:
        data=Booking(name=name,email=email,message=message,n_child=child,n_adult=adult,rooms=rooms,checkIn=checkin,checkOut=checkout,n_rooms=n_rooms)
        data.save()
        # messages.success(request,"Successfully submitted your message. We will contact you soon...")  
        return redirect('booking') 
  
  return render(request,'booking.html',{'glob':glob,'books':books})



def team(request):
  glob=GlobalSettings.objects.all()
  teams=Navigation.objects.filter(page_type="Our Team", status="Publish")
  
  return render(request,'team.html',{'glob':glob,'teams':teams})

def testimonial(request):
  glob=GlobalSettings.objects.all()
  testi =Navigation .objects.filter(page_type="Testimonial",status="Publish")
  
  return render(request,'testimonial.html',{'glob':glob,'testi':testi})

def contact(request):
    cont = Navigation.objects.filter(status='Publish', page_type='Contact')
    glob = GlobalSettings.objects.all()
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        if len(name)<2 or len(email)<3 or len(subject)<4 or len(message)<2:
            messages.error(request,"Cannot submit your message. Something went wrong.")

        else:
            data=Contact(name=name,email=email,subject=subject,message=message)
            data.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...")           
            
        
    
    return render(request, "contact.html", {'cont' : cont, 'glob': glob,}) 
  
   
