from django.shortcuts import render,HttpResponseRedirect,redirect
from home.models import pdM,attM,Category,adM,cocuM,excoM,plcM
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
            user_cocurricular = cocuM.objects.filter(user_profile=user_profile)
            user_exco = excoM.objects.filter(user_profile=user_profile)
            placement_details = plcM.objects.all()
            
            
            # print(user_attendance)
            grouped_attendance = {}
            for attendance in user_attendance:
                semester_name = attendance.category.name
                if semester_name not in grouped_attendance:
                    grouped_attendance[semester_name] = []
                grouped_attendance[semester_name].append(attendance)
            # print(grouped_attendance)
            
            return render(request, 'home/homes.html', {'user_profile': user_profile,'grouped_attendance':grouped_attendance, 'user_ad':user_ad,'user_cocurricular':user_cocurricular,'user_exco':user_exco,'placement_details': placement_details})
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

def oa(request):
    return render(request,'oa.html')
    #return HttpResponse('this is services page')
    
    
@login_required(login_url='landingpage')  
def plc(request):
    if request.method == "POST":
        print(request.POST) 
        
        compname = request.POST.get('compname')
        package = request.POST.get('package')
        semester = request.POST.get('semester')
        
        # user_profile = pdM.objects.get(RN=request.user.username)
        if compname and package and semester:
            # user_instance = user_profile.user
            user_profile = request.user.pdm
            placement_data = plcM(compname=compname, package=package, semester=semester, user_profile=user_profile)
            placement_data.save()
            messages.success(request, "Placement data submitted successfully!")
            # return redirect('home/homes')  # Redirect to home page or any other page
        else:
            messages.error(request, "Please provide all required information.")
    return render(request, 'plc.html')
    # return render(request,'plc.html')
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
            # return redirect('/homes')  # Redirect to homes page after successful upload
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
        user_cocurricular = cocuM.objects.filter(user_profile=user_profile)
        user_exco = excoM.objects.filter(user_profile=user_profile)
        placement_details = plcM.objects.all()
        # user_attendance = attM.objects.filter(category__name=user_profile.dep, month__isnull=False)

        grouped_attendance = {}
        for attendance in user_attendance:
            semester_name = attendance.category.name
            if semester_name not in grouped_attendance:
                grouped_attendance[semester_name] = []
            grouped_attendance[semester_name].append(attendance)
        
        return render(request, 'home/homes.html', {
            'user_profile': user_profile,
            'user_attendance': user_attendance,
            'user_ad': user_ad,  # Pass user_ad to the template context
            'grouped_attendance': grouped_attendance,
            'user_cocurricular': user_cocurricular,
            'user_exco': user_exco,
            'placement_details': placement_details 
        })
        
    except pdM.DoesNotExist:
        messages.error(request, "User profile does not exist.")  
        return redirect('landing.html')
           
    # print("user_attendance:", user_attendance)
    # user_profile=pdM.objects.get(RN=user.username)
    
    # return render(request,'home/homes.html', {'user_profile':user_profile, 'grouped_attendance': grouped_attendance, 'user_ad':user_ad})
    
    
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


@login_required(login_url='landingpage')
def cocu(request):
    if request.method == "POST":
        sem= request.POST.get('sem')
        professional_society= request.POST.get('professional_society')
        internship= request.POST.get('internship')
        paper_published= request.POST.get('paper_published')
        
        
        user_profile = pdM.objects.get(RN=request.user.username)
        # form = CoCurricularForm(request.POST)
        cocu = cocuM(sem=sem,professional_society=professional_society, internship=internship,  paper_published= paper_published, user_profile=user_profile)
        cocu.save()
        # print(cocu)
        messages.success(request, "Co-Curricular activities submitted successfully!")
            # return redirect('home/homes')  # Redirect to home page after successful submission
    # else:
    #     form = CoCurricularForm()

    return render(request, 'cocu.html')
    
    
    # return render(request,'cocu.html')
    #return HttpResponse('this is services page')

@login_required(login_url='landingpage')
def exco(request):
    if request.method == "POST":
        # print(request.POST) 
        exsem= request.POST.get('exsem')
        sports= request.POST.get('sports')
        nss= request.POST.get('nss')
        price= request.POST.get('price')
                
        user_profile = pdM.objects.get(RN=request.user.username)
        
        if exsem:
            exco = excoM(exsem=exsem, sports=sports, nss=nss, price=price, user_profile=user_profile)
            exco.save()
            messages.success(request, "Extra-Curricular activities submitted successfully!")
        else:
            messages.error(request, "Semester field is required.")
        
    return render(request,'exco.html')
    #return HttpResponse('this is services page')



# def fetch(request):
    # fetchdata = pdM.objects.all()
    # return render(request, 'home/homes.html', {'fetchdata': fetchdata})