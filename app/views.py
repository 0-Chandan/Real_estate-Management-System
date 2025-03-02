from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Submitproperty
from .models import Contacts,Feedback,Booking
from django.contrib import messages
from django.core.mail import send_mail
import datetime
# Create your views here.
def index(request):
    data=Submitproperty.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def Register(request):
    if request.method=="POST":
        uname=request.POST.get("uname",)
        email=request.POST.get("email")
        phone_no=request.POST.get("phone_no")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        print(uname,email,phone_no,password)
        if password!=cpassword:
            return redirect("/")
        try:
            if User.objects.get(username=uname):
                return redirect("/")
        except:
            pass
        try:
            if User.objects.get(email=email):
                return redirect("/")
        except:
            pass
        query=User.objects.create_user(uname,email,password)
        query.save()
        subject = "About Registration"
        message = f"Hi {uname}, You has been Registered successfully in the RealEstate Website"
        email_from="chandankrhzb2005@gmail.com"
        rec_list=[email,]
        send_mail(subject,message,email_from,rec_list)
        messages.success(request,"Your Registration Successfully")
        return redirect("/")
    return render(request,"register.html")

def handlelogin(request):
    if request.method=="POST":
         uname=request.POST.get("uname")
         password=request.POST.get("password")
         myuser=authenticate(username=uname,password=password)
         if myuser is not None:
             login(request,myuser)
             messages.success(request,"LOGIN SUCCESSFULLY, WELCOME Mr./Mrs. "+uname )
             return redirect("/")
         else:
             messages.success(request,"Invalid Password or Username")
             return redirect("/hlogin")
    return render(request,"login.html")
def contact(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        phone_no=request.POST.get("phone_no")
        subject=request.POST.get("subject")
        comment=request.POST.get("comment")
        print(uname,email,phone_no,subject,comment)
        query=Contacts(name=uname,email=email,phone=phone_no,subject=subject,comment=comment)
        query.save()
        messages.success(request,"Contact successfully")
        return redirect("/contact")
      
    return render(request,"contact.html")
def agent(request):
    return render(request,"agent.html")
def about(request):
    return render(request,"about.html")
def property(request):
    data=Submitproperty.objects.all()
    context={"data":data}
    return render(request,"property.html",context)
def handlelogout(request):
    logout(request)
    messages.success(request,"LOGOUT SUCCESSFULLY")
    return redirect("/")
# for property
def submit_property(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        property_type=request.POST.get("propertytype")
        bhk=request.POST.get("bhk")
        status=request.POST.get("status")
        bedroom=request.POST.get("bedroom")
        kitchen=request.POST.get("kitchen")
        bathroom=request.POST.get("bathroom")
        hall=request.POST.get("hall")
        balcony=request.POST.get("balcony")
        # Price and location
        floor=request.POST.get("floor")
        price=request.POST.get("price")
        areasize=request.POST.get("areasize")
        city=request.POST.get("city")
        address=request.POST.get("address")
        state=request.POST.get("state")
        feature=request.POST.get("feature")
        # Images and Status
        img1=request.FILES["img1"]
        img2=request.FILES["img2"]
        img3=request.FILES["img3"]
        img4=request.FILES["img4"]
        img5=request.FILES["img5"]
        floorplanimg=request.FILES["floorplanimg"]
        status2=request.POST.get("status2")
        groundfloor=request.FILES["groundfloor"]
        basementfloor=request.FILES["basementfloor"]
        isfeature=request.POST.get("isfeature")
        date=request.POST.get("date")
        ownername=request.POST.get("ownername")
        query=Submitproperty(
            title=title,content=content,property_type=property_type, bhk=bhk,status=status,
            bedroom=bedroom,kitchen=kitchen,bathroom=bathroom,hall=hall,balcony=balcony,floorap=floor,
            price=price,area_size=areasize,city=city,Address=address,state=state,feature=feature,
            img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,floor_planimg=floorplanimg,
         status2=status2,groundfloorimg=groundfloor,basementfloor=basementfloor,
            isfeatured=isfeature,date=date,ownername=ownername

        )
        print(img1)
        query.save()
        return redirect("/")

    return render(request,"submit-property.html")
# myproperty
def myproperty(request):
    data=Submitproperty.objects.all()
    context={"data":data}
    return render(request,"myproperty.html",context)
# for Editing
def edit_property(request,id):
    if request.method=="POST":
        # basic Information
        title=request.POST["title"]
        content=request.POST["content"]
        property_type=request.POST["propertytype"]
        bhk=request.POST["bhk"]
        status=request.POST["status"]
        bedroom=request.POST["bedroom"]
        kitchen=request.POST["kitchen"]
        bathroom=request.POST["bathroom"]
        hall=request.POST["hall"]
        balcony=request.POST["balcony"]
        # Price and location
        floor=request.POST["floor"]
        price=request.POST["price"]
        areasize=request.POST["areasize"]
        city=request.POST["city"]
        address=request.POST["address"]
        state=request.POST["state"]
        feature=request.POST["feature"]
        # Images and Status
        img1=request.FILES["img1"]
        img2=request.FILES["img2"]
        img3=request.FILES["img3"]
        img4=request.FILES["img4"]
        img5=request.FILES["img5"]
        floorplanimg=request.FILES["floorplanimg"]
        status2=request.POST["status2"]
        groundfloor=request.FILES["groundfloor"]
        basementfloor=request.FILES["basementfloor"]
        isfeature=request.POST["isfeature"]
        date=request.POST["date"]
        ownername=request.POST["ownername"]
        edit=Submitproperty.objects.get(id=id)
         # basic Information
        edit.title=title
        edit.content=content
        edit.property_type=property_type
        edit.bhk=bhk
        edit.status=status
        edit.bedroom=bedroom
        edit.kitchen=kitchen
        edit.bathroom=bathroom
        edit.hall=hall
        edit.balcony=balcony
        #price and location
        edit.floorap=floor
        edit.price=price
        edit.area_size=areasize
        edit.city=city
        edit.Address=address
        edit.state=state
        edit.feature=feature
        edit.img1=img1
        edit.img2=img2
        edit.img3=img3
        edit.img4=img4
        edit.img5=img5
        edit.floor_planimg=floorplanimg
        edit.status2=status2
        edit.groundfloorimg=groundfloor
        edit.basementfloor=basementfloor
        edit.isfeatured=isfeature
        edit.date=date
        edit.ownername=ownername
        edit.save()
        return redirect("/")
    data=Submitproperty.objects.get(id=id)
    context={"data":data}
    return render(request,"edit_property.html",context)
# for Deleting 
def delete_property(request,id):
    data=Submitproperty.objects.get(id=id)
    data.delete()
    return redirect("/myproperty")
# for searching 
def search(request):
    data=Submitproperty.objects.all()
    if request.method=="GET":
        query=request.GET.get("query")
        if query!=None:
            data_city=Submitproperty.objects.filter(city__icontains=query)
            data_property_type=Submitproperty.objects.filter( property_type__icontains=query)
            data_address=Submitproperty.objects.filter(Address__icontains=query)
            data_state=Submitproperty.objects.filter(state__icontains=query)
            data=data_city.union(data_property_type,data_address,data_state)
        if len(query)>72:
            messages.error(request,"Sorry! cant search your query because your searh query has too long")
        elif data.count()==0:
                messages.error(request,"No search results found.Please refine your query")   
    context={"data":data}
    return render(request,"search.html",context)
# Property details
def view_details(request,id):
    data=Submitproperty.objects.get(id=id)
    context={"data":data}
    # FOR FEEDBACK
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        feedback=request.POST.get("feedback")
        query2=Feedback(fullname=name,phone=phone,feedback=feedback)
        query2.save()
        return redirect("/")
    # for CALCULATING INSTALLMENT
    if request.method=="POST":
        p=request.POST.get("price")
        d=request.POST.get("duration")
        i=request.POST.get("interest")
        print(p,d,i)
    return render(request,"view_details.html",context)
def installment(request):
    if request.method=="POST":
        p=float(request.POST.get("price"))
        d=float(request.POST.get("duration"))
        i=float(request.POST.get("interest"))
        s=(p*d*i)/1000
        t=p+s
        m=t/12
        s=str(s)
        t=str(t)
        m=str(m)
        p1=str(p)
        d1=str(d)
        i1=str(i)
        messages.success(request,p1)
        messages.success(request,d1)
        messages.success(request,i1)
        messages.success(request,s)
        messages.success(request,t)
        messages.success(request,m)        
    return render(request,"installment.html")
# For BOOKING
def booking_now(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        alphone=request.POST.get("alphone")
        fulladdress=request.POST.get("address")
        propertyname=request.POST.get("propertyname")
        Bookingapartment=Booking(name=name,email=email,phone=phone,alternative_phone=alphone,address=fulladdress,propertyname=propertyname)
        Bookingapartment.save()
        subject = "About Booking Property"
        message = f"Dear {name},Thank you for choosing {propertyname}! We are delighted to confirm your booking."
        email_from="chandankrhzb2005@gmail.com"
        rec_list=[email,]
        send_mail(subject,message,email_from,rec_list)
        messages.success(request,"Congratulations! Your order has confirmed ")
        return redirect("/")
    return render(request,"booking-now.html")
