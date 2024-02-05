from django.shortcuts import render,HttpResponseRedirect,redirect
from home.models import pdM,attM,Category,adM
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import AcademicDetailsForm


# Create your views here.

def landingpage(request):
    return render(request,'landing.html')
    #return HttpResponse('this is services page')

def loginpage(request):
    if request.method =='POST':
        unamel=request.POST.get('unamel')
        pwl=request.POST.get('pwl')
        # print(unamel,pwl)
        user=authenticate(request, username=unamel,password=pwl)
        
        if user is not None:
            login(request,user)
            user_profile = pdM.objects.filter(RN=user.username).first()
            user_attendance=attM.objects.filter(user_profile=user_profile)
            user_ad = adM.objects.filter(user=user)
            
            
            # print(user_attendance)
            grouped_attendance = {}
            for attendance in user_attendance:
                semester_name = attendance.category.name
                if semester_name not in grouped_attendance:
                    grouped_attendance[semester_name] = []
                grouped_attendance[semester_name].append(attendance)
            # print(grouped_attendance)
            
            return render(request, 'home/homes.html', {'user_profile': user_profile,'grouped_attendance':grouped_attendance, 'user_ad':user_ad})
            # return render(request,'home/homes.html',{'user': user})
        else:
            messages.success(request, "Incorrect username or password!")
            # return HttpResponse('Incorrect!')
        
    return render(request,'login.html')

def signuppage(request):
    if request.method =='POST':
        uname=request.POST.get('uname')
        email= request.POST.get('email')
        pw= request.POST.get('pw')
        Cpw= request.POST.get('Cpw')
        if pw != Cpw:
            messages.success(request, "Password doesn't match!")
        else:
            my_user=User.objects.create_user(uname,email,pw)
            my_user.save()
            return HttpResponseRedirect(reverse('loginpage'))
    # return HttpResponse("User has been created successfully!")
    return render(request,'login.html')
    
    
def logoutpage(request):
    logout(request)    
    return redirect('landingpage')


@login_required(login_url='landingpage') 
def index(request):
    # messages.success(request,"this is test message.")
    return render(request,'index.html')
   # return HttpResponse('this is home page')


@login_required(login_url='landingpage') 
def pd(request):
    if request.method == "POST":
        Fname= request.POST.get('Fname')
        RN=request.POST.get('RN')
        DOB=request.POST.get('DOB')
        Email=request.POST.get('Email')
        MN=request.POST.get('MN')
        Gen=request.POST.get('Gen')
        Caddr=request.POST.get('Caddr')
        Paddr=request.POST.get('Paddr')
    
        Ftname=request.POST.get('Ftname')
        Email1=request.POST.get('Email1')
        MN1=request.POST.get('NM1')
    
        Mtname=request.POST.get('Mtname')
        Email2=request.POST.get('Email2')
        MN2=request.POST.get('MN2')
    
        Stdmentor=request.POST.get('Stdmentor')
        EmailM=request.POST.get('EmailM')
        MNstdm=request.POST.get('MNstdm')
    
        Factmentor=request.POST.get('Factmentor')
        EmailF=request.POST.get('EmailF')
        MNfactm=request.POST.get('MNfactm')
    
        dep=request.POST.get('dep')
        
        Pd =pdM(Fname=Fname,RN=RN, DOB=DOB, Email=Email, MN=MN, Gen=Gen, Caddr=Caddr, Paddr=Paddr, Ftname=Ftname, Email1=Email1, MN1=MN1, Mtname=Mtname, Email2=Email2, MN2=MN2, Stdmentor=Stdmentor, EmailM=EmailM, MNstdm=MNstdm, Factmentor=Factmentor, EmailF=EmailF, MNfactm=MNfactm, dep=dep)
        
        Pd.save()
        messages.success(request, "Profile details uploaded!")
             
    return render(request,'PD.html')
    #return HttpResponse('this is about page')

def services(request):
    return render(request,'services.html')
    #return HttpResponse('this is services page')

@login_required(login_url='landingpage') 
def ad(request):
    if request.method == "POST":
        form = AcademicDetailsForm(request.POST)
        if form.is_valid():
            academic_details = form.save(commit=False)
            academic_details.user = request.user
            academic_details.save()
            messages.success(request, "Academic details uploaded!")
            # return redirect('home/homes')  # Redirect to homes page after successful upload
    else:
        form = AcademicDetailsForm(initial={'user': request.user})
    
    return render(request,'AD.html',{'form':form})
    #return HttpResponse('this is contact page')
    
    
@login_required(login_url='landingpage')    
def homes(request):
    user=request.user
        
    try:
        user_profile = pdM.objects.get(RN=user.username)
        user_attendance=attM.objects.filter(user_profile=user_profile)
        user_ad = adM.objects.filter(user=user)
        # user_attendance = attM.objects.filter(category__name=user_profile.dep, month__isnull=False)

        
    except pdM.DoesNotExist:
        user_profile = None
        user_attendance=None
     
    grouped_attendance = {}
    for attendance in user_attendance:
        semester_name = attendance.category.name
        if semester_name not in grouped_attendance:
            grouped_attendance[semester_name] = []
        grouped_attendance[semester_name].append(attendance)
           
    print("user_attendance:", user_attendance)
    # user_profile=pdM.objects.get(RN=user.username)
    
    return render(request,'home/homes.html', {'user_profile':user_profile, 'grouped_attendance': grouped_attendance, 'user_ad':user_ad})
    
    
@login_required(login_url='landingpage') 
def att(request):
    if request.method == "POST":
        month= request.POST.get('month')
        percentage= request.POST.get('percentage')
        # category= request.POST.get('category')
        
        user_profile = pdM.objects.get(RN=request.user.username)
        category_name = request.POST.get('category')
        
        category_instance, created = Category.objects.get_or_create(name=category_name)
        
        if attM.objects.filter(category=category_instance, user_profile=user_profile).count() >= 3:
            messages.error(request, "The Semester can be only selected thrice !")
        else:
            att = attM(month=month, percentage=percentage, category=category_instance, user_profile=user_profile)
            att.save()
            messages.success(request, "Attendance details uploaded successfully!")

        
    return render(request,'att.html')
    #return HttpResponse('this is services page')


# def fetch(request):
    # fetchdata = pdM.objects.all()
    # return render(request, 'home/homes.html', {'fetchdata': fetchdata})