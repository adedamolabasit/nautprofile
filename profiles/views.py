from datetime import datetime
from django.shortcuts import redirect,render,get_object_or_404
from .models import Profile,Gallery
from random import randint
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings
import csv
from django.http import HttpResponse,FileResponse
from django.urls import reverse
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from reportlab.pdfgen import canvas
from django.contrib import messages
import io

# Create your views here.




def index(request):
    gallery=Gallery.objects.all()
    now=datetime.now()
    heading='Gallery'
    details='Why I say old chap that is spiffing off his nut arse pear shaped plasteredJeffrey bodge barney some dodgy.!!'
   
    return render(request,'gallery.html',{'query':gallery,now:now,'heading':heading,'details':details})

def profile(request,slug):  
    query=get_object_or_404(Profile,user_id=slug)
    now=datetime.now()
    ip , is_routable  = get_client_ip(request)
    if ip is None :
        ip ="0.0.0.0"
    else:
        if is_routable:
            ipv="Public"
        else:
            ipv='Private'
    try :
        response = DbIpCity.get(ip.api_key == 'free')
        location=response.country + "|" + response.city
    except:
        location='unknown'
    send_mail(
        'Nautilus QR_CODE Scanned',
        f"""
The system detected that a Nautilus Technologies ID CARD had been scanned.
Name:{query.firstname } {query.lastname }
Time:{now}
Device IP Address:{ip}
location:{location}
Take this security warning carefully.
                """,
        'Nautilus Security',
        ['adedamolabasit09@gmail.com','ayowole.ogunsade@nautilus.tech','hr@nautilus.tech'],
        
    )
   

    link=F'127.0.0.1:8000/{slug}'
    query2=Profile.objects.all().exclude(user_id=slug)
    

    print(ip,ipv)
    print(location)
    return render(request,'testimonial.html',{'query':query,'link':link,'query2':query2})
def profile_personal(request,slug):  
    query=get_object_or_404(Profile,user_id=slug)
    now=datetime.now()
    print(request.path)
    link=F'127.0.0.1:8000/{slug}'
    query2=Profile.objects.all().exclude(user_id=slug)
    return render(request,'testimonial.html',{'query':query,'link':link,'query2':query2})


def add_profile(request):
    heading='Upload a Profile'
    details=''
    if request.method == "POST": 
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        profession=request.POST.get('profession')
        email=request.POST.get('email')
        query_name=Profile.objects.filter(firstname=firstname,lastname=lastname)
        file = request.FILES.get('file',None)
        if file:
            picture=file
        elif file is None:
            messages.info(request,'Upload an Image')
     

        if query_name.exists():
            messages.info(request,'user already exists')
          

        else:
            random=randint(1000,99999)
            user_id=F"NAT{str(random)}"
            query_id=Profile.objects.filter(user_id=user_id)
            while len(query_id) != 0:
                random=randint(1000,9999)
                user_id=F"NAUT{str(random)}"
            profile=Profile.objects.create(firstname=firstname,lastname=lastname,
            profession=profession,email=email,user_id=user_id,picture=picture)
            profile.save()
          

            response=HttpResponse(content_type='txt/csv')
            response['Content-Disposition']="attachment;filename=f'nautilus-profile-{fistname}-{lastname}.csv"
            writer=csv.writer(response)       
            writer.writerow(['FIRST NAME',firstname])
            writer.writerow(['LAST NAME',lastname])
            writer.writerow(['USER ID',user_id])
            
            return response

    else:
       pass




# Create your views here.
           
            
            # buffer = io.BytesIO()
            # x = canvas.Canvas(buffer)
            # x.drawString(100, 100, 'Instruction')
            # x.drawString(100, 200, 'this is the full instruction')
            # x.showPage()
            # x.save()
            # buffer.seek(0)
            # return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')
          
        
    return render(request,'form.html',{'heading':heading,'details':details})
def csv_file(firstname,lastname,user_id):
    response=HttpResponse(content_type='txt/csv')
    response['Content-Disposition']="attachment:filename='nautilus.csv'"
    writer=csv.writer(response)       
    writer.writerow([firstname,lastname,user_id])
    return response

def edit_profile(request,slug):
    profile=Profile.objects.filter(user_id=slug).first()
    if request.method == "POST": 
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        profession=request.POST.get('profession')
        email=request.POST.get('email')
        # about=request.POST.get('about')
        profile=Profile.objects.filter(user_id=slug)
        if profile is None:
            messages.info(request,'user not found')
            # error="user not found"
            # return render(request,'error.html',{'error':error})
        file = request.FILES.get('file',None)
        if file is not None:
            # fs = FileSystemStorage()
            # filename=fs.save(file.name,file)
            # url=fs.url(filename)
            picture=file
        else:
            messages.info(request,'Upload an Image')
            # error="Upload Image"
            # return render(request,'error.html',{'error':error})
        profile.firstname=firstname
        profile.lastname=lastname
        profile.email=email
        # profile.about=about
        profile.profession=profession
        profile.picture=picture
      
        profile.update()
        return redirect(reverse('profile',kwargs={'slug':slug}))
    if request.method =="GET":
    
        print(profile.lastname)
        return render(request,'edit_form.html',{'profile':profile})
    return render(request,'edit_form.html')

def team(request):
    query=Profile.objects.all()
    return render(request,'team.html',{'query':query})


def add_gallery(request):
    heading='Upload Images'
    details=''
    file = request.FILES.get('file')
    if request.method == 'POST':         
        if file is not None:     
            # fs = FileSystemStorage()
            # filename=fs.save(file.name,file)
            # url=fs.url(filename)
            picture=file
            image=Gallery(picture=picture)
            image.save()
        else:
            messages.info(request,'Upload an Image')
            # error="Upload Image"
            # return render(request,'error.html',{'error':error})
    else:
        return render(request,'add_gallery.html',{'heading':heading,'details':details})
    return render(request,'add_gallery.html',{'heading':heading,'details':details})


def prompt(request):
    if request.method == 'POST':
        user_id=request.POST.get('id')
        query=Profile.objects.filter(user_id=user_id).first()
        if query is not None :
            return redirect(reverse('profile',kwargs={'slug':query.user_id}))
        else:
            messages.info(request,'invalid user id')
    else:
        return render(request,'prompt.html',{})
    return render(request,'prompt.html',{})
