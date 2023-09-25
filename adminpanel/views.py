from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import GlobalSettings, Contact, Navigation,Booking,Rooms_detail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse


def admin_login(request):
    glob = GlobalSettings.objects.all()
    try:
        # messages.info(request, 'Account not found')
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")         
            user_obj = User.objects.filter(username = username)
            
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            print(username, password)
            user_obj = authenticate(username = username, password = password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect("dashboard")
          
            messages.info(request, "Invalid password")
            return redirect('/')
                    
        return render(request, "login.html", {'glob':glob})
       
    except Exception as e:
        print(e)
        # Add a proper response in case of an exception
        return HttpResponse("An error occurred")

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    glob = GlobalSettings.objects.all()

    return render(request, "dashboard.html", {'glob':glob})

def Logoutpage(request):
    logout(request)
    return redirect("admin_login")

@login_required(login_url=settings.LOGIN_URL)
def globalsetting(request):
    glob = GlobalSettings.objects.all()
    try:
        data = GlobalSettings.objects.first()
    except GlobalSettings.DoesNotExist:
        data = None

    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        description = request.POST.get('description')
        facebooklink = request.POST.get('facebooklink')
        linkdinlink = request.POST.get('linkdinlink')
        instagramlink = request.POST.get('instagramlink')
        logo = request.FILES.get('logo')
        back_image = request.FILES.get('back_image')
        

        if data is None:
            # Create a new GlobalSettings object
            data = GlobalSettings(SiteName=name, SiteContact=contact, SiteAddress=address, SiteEmail=email,
                                  Sitedescription=description,Sitefacebooklink=facebooklink,Sitelinkdinlink=linkdinlink,Siteinstagramlink=instagramlink)
        else:
            # Update existing GlobalSettings object
            data.SiteName = name
            data.SiteContact = contact
            data.SiteAddress = address
            data.SiteEmail = email
            data.Sitedescription = description
            data.Sitefacebooklink = facebooklink
            data.Sitelinkdinlink = linkdinlink
            data.Siteinstagramlink = instagramlink

        if logo:
            # Set the uploaded image to the 'logo' field
            data.logo = logo
        if back_image:
            data.back_image = back_image
        
        data.save()

        return redirect('globalsetting')  # Redirect to the same view after saving the data

    return render(request, "globalsetting.html", {"data": data, 'glob' : glob})

@login_required(login_url=settings.LOGIN_URL)
def contact_us(request):
    glob = GlobalSettings.objects.all()
    con=Contact.objects.all()
 
    return render(request, "contactus.html",{'con':con, 'glob' : glob})

@login_required(login_url=settings.LOGIN_URL)
def delete_contact(request, pk):
    con = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        con.delete()
        return redirect('contactus')

    return redirect('contactus')

@login_required(login_url=settings.LOGIN_URL)
def main_navigation(request, parent_id=None):
    glob=GlobalSettings.objects.all()
        
    if parent_id:
        obj = Navigation.objects.filter(Parent=parent_id).order_by('position')
    else:
        obj = Navigation.objects.filter(Parent = None).order_by('position')
 
    return render(request, "main_navigation.html", {'obj':obj, 'parent_id':parent_id,'glob':glob})

@login_required(login_url=settings.LOGIN_URL)
def navigation_list(request, parent_id=None):
    glob = GlobalSettings.objects.all()
    obj = Navigation.objects.all()

    if request.method == "POST":
        # Retrieve form data
        # next = request.POST.get('next','/')
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        status = request.POST.get('status')
        position = request.POST.get('position')
        page_type = request.POST.get('page_type')
        title = request.POST.get('title')
        short_desc = request.POST.get('short_desc')
        bannerimage = request.FILES.get('bannerimage')
        brochure = request.FILES.get('brochure')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        icon_image = request.POST.get('icon_image')
        slider_image = request.FILES.get('slider_image')
        parent_id = request.POST.get('Parent')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')

        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        # Create a new Navigation objectj
        obj = Navigation.objects.create(
            name=name,
            caption=caption,
            status=status,
            position=position,
            page_type=page_type,
            title=title,
            short_desc=short_desc,
            meta_title=meta_title,
            meta_keyword=meta_keyword,
            desc=desc,
            icon_image=icon_image,
            image=image,
            Parent=parent_navigation,  # Assign parent navigation object
        )
        # obj.Parent = Navigation.objects.filter(id=parent_id)

        # Set uploaded images
        if bannerimage:
            obj.bannerimage = bannerimage
        if image:
            obj.image = image
        if slider_image:
            obj.slider_image = slider_image
        if brochure:
            obj.brochure = brochure

        obj.save()  # Save the new Navigation object to the database

        obj = Navigation.objects.all()  # Update the navigation list with the new object

        if parent_id:
            return redirect('main_navigation', parent_id=parent_id )
        else:
            return redirect('main_navigation')
      

    return render(request, 'navigation.html',{'obj': obj, 'glob' : glob, 'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def update(request, pk):
    glob = GlobalSettings.objects.all()
    data = get_object_or_404(Navigation, pk=pk)

    if request.method == "POST":
        name=request.POST.get('name')
        caption=request.POST.get('caption')
        status=request.POST.get('status')
        position=request.POST.get('position')
        page_type=request.POST.get('page_type')
        title=request.POST.get('title')
        short_desc=request.POST.get('short_desc')
        desc=request.POST.get('desc')
        bannerimage=request.FILES.get('bannerimage')
        meta_title=request.POST.get('meta_title')
        meta_keyword=request.POST.get('meta_keyword')
        icon_image=request.POST.get('icon_image')
        slider_image=request.FILES.get('slider_image')
        brochure = request.FILES.get('brochure')
        parent_id = request.POST.get('Parent')
        image = request.FILES.get('image')
        

        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        
        # Update the object with the form data
        data.name = name
        data.caption = caption
        data.status = status
        data.position = position
        data.page_type = page_type
        data.title = title
        data.short_desc = short_desc
        data.meta_title = meta_title
        data.meta_keyword = meta_keyword
        data.desc = desc
        data.Parent=parent_navigation
        data.icon_image=icon_image

        if bannerimage:
            data.bannerimage = bannerimage

        if image:
            data.image = image

        if slider_image:
            data.slider_image = slider_image
        
        if brochure:
            data.brochure = brochure
        
        data.save()

        if parent_id:
            return redirect('main_navigation', parent_id=parent_id )
        else:
            return redirect('main_navigation')
        
    parent_id = data.Parent.id if data.Parent else None

    return render(request, 'update.html', {'data': data,'glob':glob,'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def delete_nav(request, pk):
    obj = get_object_or_404(Navigation, pk=pk)
    parent_id = None

    if request.method == "POST":
        parent_id = obj.Parent.id if obj.Parent else None
        obj.delete()

    if parent_id:
        return redirect('main_navigation', parent_id=parent_id)
    else:
        return redirect('main_navigation')
    
    # return render(request, 'delete.html', {'obj': obj})





@login_required(login_url=settings.LOGIN_URL)
def bookings(request):
    glob = GlobalSettings.objects.all()
    book=Booking.objects.all()
 
    return render(request, "bookings.html",{'book':book, 'glob' : glob})

@login_required(login_url=settings.LOGIN_URL)
def delete_bookings(request, pk):
    book = get_object_or_404(Booking, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('bookings')

    return redirect('bookings')

@login_required(login_url=settings.LOGIN_URL)
def room_details(request):
    glob = GlobalSettings.objects.all()
    r_detail=Rooms_detail.objects.all()
    
    return render(request,'room_list.html',{'glob' : glob,'r_detail':r_detail})

@login_required(login_url=settings.LOGIN_URL)
def room_create(request):
    glob = GlobalSettings.objects.all()
      
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        n_bed = request.POST.get('n_bed')
        n_bath = request.POST.get('n_bath')  
        wifi = request.POST.get('wifi')
        price =request.POST.get('price')
        
        r_detail=Rooms_detail.objects.create(
            description=description,
            n_bed=n_bed,
            n_bath=n_bath,
            wifi=wifi,
            price=price,
            name=name   
        )
        if image:
            r_detail.image=image
        
        
        r_detail=r_detail.save()
        
        return redirect('room_details')
    
    return render(request, 'create_room.html',{'glob':glob})

def room_update(request,pk):
    glob = GlobalSettings.objects.all()
    r_detail = get_object_or_404(Rooms_detail,pk=pk)
      
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        n_bed = request.POST.get('n_bed')
        n_bath = request.POST.get('n_bath')  
        wifi = request.POST.get('wifi')
        price =request.POST.get('price')
        
        
        r_detail.name=name
        r_detail.description=description
        r_detail.n_bed=n_bed
        r_detail.n_bath=n_bath
        r_detail.wifi=wifi
        r_detail.price=price
        
        if image:
            r_detail.image=image
            
        r_detail.save()
        
        return redirect('room_details')
    
    return render(request, 'update_room.html',{'glob':glob,'r_detail':r_detail})

@login_required(login_url=settings.LOGIN_URL)
def room_delete(request, pk):
    r_detail = get_object_or_404(Rooms_detail, pk=pk)

    if request.method == "POST":
        r_detail.delete()
        return redirect('room_details')

    return redirect('room_details')
        
        
      
        
