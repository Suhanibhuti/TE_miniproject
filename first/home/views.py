from django.shortcuts import render,HttpResponseRedirect,redirect
from home.models import pdM,attM,Category,adM,cocuM,excoM,plcM,pdmM,Student,hsM
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import AcademicDetailsForm
from .decorators import unauthenticated_user,allowed_user,student_only
from django.contrib.auth.models import Group
from django.db import IntegrityError
import os
from django.conf import settings
from django.http import JsonResponse
import json
from collections import defaultdict

# Create your views here.

def landingpage(request):
    return render(request,'landing.html')
    #return HttpResponse('this is services page')


@unauthenticated_user
# @allowed_user(allowed_roles=['Students'])
def loginpage(request):
    if request.method =='POST':
        unamel=request.POST.get('unamel')
        pwl=request.POST.get('pwl')
        # print(unamel,pwl)
        user=authenticate(request, username=unamel,password=pwl)
        
        if user is not None:
        # if user is not None and user.role == CustomUser.STUDENT:
            login(request,user)
            user_profile = pdM.objects.filter(RN=user.username).first()
            # user_attendance=attM.objects.filter(user_profile=user_profile)
            # user_ad = adM.objects.filter(user=user)
            # user_cocurricular = cocuM.objects.filter(user_profile=user_profile)
            # user_exco = excoM.objects.filter(user_profile=user_profile)
            # placement_details = plcM.objects.all()                        
            # print(user_attendance)
            # grouped_attendance = {}
            # for attendance in user_attendance:
            #     semester_name = attendance.category.name
            #     if semester_name not in grouped_attendance:
            #         grouped_attendance[semester_name] = []
            #     grouped_attendance[semester_name].append(attendance)
            # print(grouped_attendance)
            
            return redirect('homes')
            
            # return render(request, 'home/homes.html', {'user_profile': user_profile,'grouped_attendance':grouped_attendance, 'user_ad':user_ad,'user_cocurricular':user_cocurricular,'user_exco':user_exco,'placement_details': placement_details})
            # return render(request,'home/homes.html',{'user': user})
        else:
            messages.error(request, "Incorrect username or password!")
            # return HttpResponse('Incorrect!')
        
    return render(request,'login_S.html')



# @unauthenticated_user
def signuppage(request):
    if request.method =='POST':
        uname=request.POST.get('uname')
        email= request.POST.get('email')
        pw= request.POST.get('pw')
        Cpw= request.POST.get('Cpw')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return HttpResponseRedirect(reverse('signuppage'))
        
        if pw != Cpw:
            messages.error(request, "Password doesn't match!")
        else:
            try:
                my_user=User.objects.create_user(uname,email,pw)
                my_user.save()
                group, created  = Group.objects.get_or_create(name='Student')
                my_user.groups.add(group)
                return HttpResponseRedirect(reverse('loginpage'))
            except IntegrityError:
                messages.error(request, "An error occurred while creating the user.")
                return HttpResponseRedirect(reverse('signuppage'))
    # return HttpResponse("User has been created successfully!")
    return render(request,'login_S.html')
 
 
 
# @allowed_user(allowed_roles=['Mentors'])
# @unauthenticated_user
# @login_required
def loginpageM(request):
    if request.method == 'POST':
        username = request.POST.get('unamelM')
        password = request.POST.get('pwlM')
        mentor = authenticate(username=username, password=password)
        if mentor is not None:
        # if mentor is not None and mentor.role == CustomUser.MENTOR:
            login(request, mentor)
            # students = Student.objects.all()
            # student_data = Student.objects.filter(user=request.user)
            
            return redirect('homesM')
            # return render(request, 'homeM.html',{'student_data':student_data})
            # return redirect('mentor_dashboard')  # Redirect to mentor dashboard
        else:
            # Handle invalid login
            messages.error(request, "Incorrect username or password!")
            # return render(request, 'login_M.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login_M.html')
    # return render(request,'login_M.html')
    #return HttpResponse('this is services page') 
    
    
    
def signuppageM(request):
    if request.method =='POST':
        unameM=request.POST.get('unameM')
        emailM= request.POST.get('emailM')
        pwM= request.POST.get('pwM')
        CpwM= request.POST.get('CpwM')
        
        if User.objects.filter(username=unameM).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return HttpResponseRedirect(reverse('signuppageM'))
        if pwM != CpwM:
            messages.error(request, "Password doesn't match!")
        else:
            try:
                # my_user=User.objects.create_user(unameM,emailM,pwM)
                my_user=User.objects.create_user(unameM,emailM,pwM)
                my_user.save()
                group, created  = Group.objects.get_or_create(name='Mentors')
                my_user.groups.add(group)
                return HttpResponseRedirect(reverse('loginpageM'))
            except IntegrityError:
                messages.error(request, "An error occurred while creating the user.")
                return HttpResponseRedirect(reverse('signuppageM'))
    # return HttpResponse("User has been created successfully!")
    return render(request,'login_M.html')
    # return render(request,'login_M.html')
    #return HttpResponse('this is services page')  
    
    
    
def logoutpage(request):
    logout(request)    
    return redirect('landingpage')




# @login_required(login_url='landingpage') 
# @student_required
def index(request):
    # messages.success(request,"this is test message.")
    return render(request,'index.html')
   # return HttpResponse('this is home page')




@login_required(login_url='loginpage') 
# @student_required
@allowed_user(allowed_roles=['Student'])
# @unauthenticated_user
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



@login_required(login_url='loginpage') 
# @student_required
@allowed_user(allowed_roles=['Student'])
def oa(request):
    return render(request,'oa.html')
    #return HttpResponse('this is services page')
    
    
    
@login_required(login_url='loginpage') 
# @student_required 
@allowed_user(allowed_roles=['Student'])
def plc(request):
    if request.method == "POST":
        # print(request.POST) 
        
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



@login_required(login_url='loginpage') 
# @student_required 
@allowed_user(allowed_roles=['Student'])
def hs(request):
    if request.method == "POST":
        gre = request.POST.get('gre')
        tofel = request.POST.get('tofel')
        cat = request.POST.get('cat')
        others = request.POST.get('others')

        try:
            # user_profile = pdM.objects.get(RN=request.user.username)
            higher_std = hsM(gre=gre, tofel=tofel, cat=cat, others=others, user=request.user)
            higher_std.save()
            messages.success(request, "Higher studies data submitted successfully!")
        except pdM.DoesNotExist:
            messages.error(request, "User profile does not exist.")

    return render(request, 'plc.html')



@login_required(login_url='loginpage') 
# @student_required
@allowed_user(allowed_roles=['Student'])
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
    
    
    
@login_required(login_url='loginpage') 
# @student_required  
@allowed_user(allowed_roles=['Student'])
# @unauthenticated_user
def homes(request):
    user=request.user
    semester_range = range(1, 9)
        
    try:
        user_profile = pdM.objects.get(RN=user.username)
        user_attendance=attM.objects.filter(user_profile=user_profile)
        user_ad = adM.objects.filter(user=user)
        user_cocurricular = cocuM.objects.filter(user_profile=user_profile)
        user_exco = excoM.objects.filter(user_profile=user_profile)
        placement_details = plcM.objects.all()
        higher_stds = hsM.objects.filter(user=request.user)
        # user_attendance = attM.objects.filter(category__name=user_profile.dep, month__isnull=False)

        grouped_attendance = {}
        for attendance in user_attendance:
            semester_name = attendance.category.name
            if semester_name not in grouped_attendance:
                grouped_attendance[semester_name] = []
            grouped_attendance[semester_name].append(attendance)
        
        # semester_attendances = defaultdict(list)
        # for semester_num in range(1, 9):
        #     semester_attendances[semester_num] = grouped_attendance.get(str(semester_num), [])
        
        return render(request, 'home/homes.html', {
            'user_profile': user_profile,
            'user_attendance': user_attendance,
            'user_ad': user_ad,  # Pass user_ad to the template context
            'grouped_attendance': grouped_attendance,
            'user_cocurricular': user_cocurricular,
            'user_exco': user_exco,
            'placement_details': placement_details,
            'semester_range': semester_range,
            # 'semester_attendances': semester_attendances,
            'higher_stds': higher_stds
        })
        
    except pdM.DoesNotExist:
        messages.error(request, "User profile does not exist.")  
        return redirect('landing.html')
           
    # print("user_attendance:", user_attendance)
    # user_profile=pdM.objects.get(RN=user.username)
    
    # return render(request,'home/homes.html', {'user_profile':user_profile, 'grouped_attendance': grouped_attendance, 'user_ad':user_ad})
    
    
    
@login_required(login_url='loginpage') 
# @student_required
@allowed_user(allowed_roles=['Student'])
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



@login_required(login_url='loginpage')
# @student_required
@allowed_user(allowed_roles=['Student'])
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



@login_required(login_url='loginpage')
# @student_required
@allowed_user(allowed_roles=['Student'])
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



@login_required(login_url='loginpage')
@allowed_user(allowed_roles=['Mentors'])
def homesM(request):
    # students = Student.objects.all()
    current_user = request.user
    student_data = Student.objects.filter(user=current_user)
    # print(students)
    return render(request,'homeM.html',{'student_data': student_data})



@login_required(login_url='loginpage')
@allowed_user(allowed_roles=['Mentors'])
def pdm(request):
    if request.method == "POST":
        FnameM= request.POST.get('FnameM')
        IDM= request.POST.get('IDM')
        DOBM=request.POST.get('DOBM')
        EmailM=request.POST.get('EmailM')
        MNM=request.POST.get('MNM')
        GenM=request.POST.get('GenM')
        depM=request.POST.get('depM')
        Pdm = pdmM(FnameM=FnameM, IDM=IDM, DOBM=DOBM, EmailM=EmailM,MNM=MNM, GenM=GenM,depM=depM)
        Pdm.save()
        messages.success(request, "Profile details uploaded!")
    return render(request,'pdM.html')
    #return HttpResponse('this is services page')



@allowed_user(allowed_roles=['Mentors'])
@login_required(login_url='loginpage')
def report(request):
    return render(request,'reportM.html')



@allowed_user(allowed_roles=['Mentors'])
@login_required(login_url='loginpage')
def printr(request):
    if request.method == "POST":
        category =request.POST['category']
        sh =request.POST['sh']
        batch =request.POST['batch']
        sem =request.POST['sem']
        date =request.POST['date']
        stdcount =request.POST['stdcount']
        stdrn =request.POST['stdrn']
        dur1 =request.POST['dur1']
        dur2 =request.POST['dur2']
        Atdef1 =request.POST['Atdef1']
        Atdef2 =request.POST['Atdef2']
        apdef1 =request.POST['apdef1']
        apdef2 =request.POST['apdef2']
        ca1 =request.POST['ca1']
        ca2 =request.POST['ca2']
        ea1 =request.POST['ea1']
        ea2 =request.POST['ea2']
        bep1 =request.POST['bep1']
        bep2 =request.POST['bep2']
        hghs1 =request.POST['hghs1']
        hghs2 =request.POST['hghs2']
        schod1 =request.POST['schod1']
        schod2 =request.POST['schod2']
        scp1 =request.POST['scp1']
        scp2 =request.POST['scp2']
        other1 =request.POST['other1']
        other2 =request.POST['other2']
        impact =request.POST['impact']      
        
        # uploaded_file1 = request.FILES.get('img1')
        # uploaded_file2 = request.FILES.get('img2')
        # img1_url = None
        # img2_url = None
        
        # if uploaded_file1:
        #     # Handle the first uploaded file
            
        #     # Check if the file is a PDF or another allowed format
        #     if not uploaded_file1.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
        #         messages.error(request, "Only PDF, JPG, JPEG, and PNG files are allowed for Image 1.")
        #         # return HttpResponseBadRequest("Only PDF, JPG, JPEG, and PNG files are allowed for Image 1.")
        #     else:
        #         # Define the directory to save the uploaded file temporarily
        #         upload_dir = os.path.join(settings.MEDIA_ROOT, 'media')
        #         os.makedirs(upload_dir, exist_ok=True)
                
        #         # Save the uploaded file to the defined directory
        #         file_path1 = os.path.join(upload_dir, uploaded_file1.name)
        #         with open(file_path1, 'wb') as f:
        #             for chunk in uploaded_file1.chunks():
        #                 f.write(chunk)
                
        #         # Set the image URL for rendering in the template
        #         img1_url = file_path1
            
        # if uploaded_file2:
        #     # Handle the second uploaded file
            
        #     # Check if the file is a PDF or another allowed format
        #     if not uploaded_file2.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
        #         messages.error(request, "Only PDF, JPG, JPEG, and PNG files are allowed for Image 2.")
        #         # return HttpResponseBadRequest("Only PDF, JPG, JPEG, and PNG files are allowed for Image 2.")
        #     else:
        #         # Define the directory to save the uploaded file temporarily
        #         upload_dir = os.path.join(settings.MEDIA_ROOT, 'media')
        #         os.makedirs(upload_dir, exist_ok=True)
                
        #         # Save the uploaded file to the defined directory
        #         file_path2 = os.path.join(upload_dir, uploaded_file2.name)
        #         with open(file_path2, 'wb') as f:
        #             for chunk in uploaded_file2.chunks():
        #                 f.write(chunk)
                
        #         # Set the image URL for rendering in the template
        #         img2_url = file_path2
            
            
        # print(category,sh,batch,sem,date,stdcount,stdrn,dur1,dur2,Atdef1,Atdef2,apdef1,apdef2,ca1,ca2,ea1,ea2,bep1,bep2,hghs1,hghs2,schod1,schod2,scp1,scp2,other1,other2,impact,img1,img2)
        
        # return render(request,'printr.html',{'category': category ,'sh': sh ,'batch': batch ,'sem': sem ,'date': date ,'stdcount': stdcount ,'stdrn': stdrn ,'dur1' : dur1 ,'dur2' : dur2 ,'Atdef1' : Atdef1 ,'Atdef2': Atdef2 ,'apdef1': apdef1 ,'apdef2': apdef2 ,'ca1': ca1 ,'ca2': ca2 ,'ea1': ea1 ,'ea2': ea2 ,'bep1' : bep1 ,'bep2': bep2 ,'hghs1': hghs1 ,'hghs2': hghs2 ,'schod1': schod1 ,'schod2': schod2,'scp1': scp1 ,'scp2': scp2 ,'other1': other1 ,'other2':other2 ,'impact': impact ,'img1_url': img1_url ,'img2_url':img2_url})
        
        return render(request,'printr.html',{'category': category ,'sh': sh ,'batch': batch ,'sem': sem ,'date': date ,'stdcount': stdcount ,'stdrn': stdrn ,'dur1' : dur1 ,'dur2' : dur2 ,'Atdef1' : Atdef1 ,'Atdef2': Atdef2 ,'apdef1': apdef1 ,'apdef2': apdef2 ,'ca1': ca1 ,'ca2': ca2 ,'ea1': ea1 ,'ea2': ea2 ,'bep1' : bep1 ,'bep2': bep2 ,'hghs1': hghs1 ,'hghs2': hghs2 ,'schod1': schod1 ,'schod2': schod2,'scp1': scp1 ,'scp2': scp2 ,'other1': other1 ,'other2':other2 ,'impact': impact })
        
        
    return render(request,'reportM.html')



@allowed_user(allowed_roles=['Mentors'])
@login_required
def studentData(request,roll_number):
    # current_user = request.user
    # user_profile = pdM.objects.filter(RN=roll_number, user=current_user).first()
    user_profile = pdM.objects.filter(RN=roll_number).first()
    user_attendance=attM.objects.filter(user_profile=user_profile)
    user_ad = adM.objects.filter(user=request.user)
    user_cocurricular = cocuM.objects.filter(user_profile=user_profile)
    user_exco = excoM.objects.filter(user_profile=user_profile)
    placement_details = plcM.objects.all()
    
    grouped_attendance = {}
    for attendance in user_attendance:
                semester_name = attendance.category.name
                if semester_name not in grouped_attendance:
                    grouped_attendance[semester_name] = []
                grouped_attendance[semester_name].append(attendance)
    return render(request,'studentData.html',{'user_profile':user_profile,'grouped_attendance':grouped_attendance,'user_ad':user_ad,'user_cocurricular':user_cocurricular,'user_exco':user_exco,'placement_details': placement_details})



@login_required
def get_data(request):
    roll_number = request.GET.get('rollNumber')  # Get the roll number from the request parameters
    # print("Received Roll Number:", roll_number) 
    if roll_number:
        # Query the pdM table to filter by the provided roll number
        student = pdM.objects.filter(RN=roll_number).values().first()  # Get the first matching student
        if student:
            # Assuming 'Fname' is the correct key for the name field in your pdM model
            # print("Found Student Details - Roll Number:", student['RN'], ", Name:", student['Fname'])
            return JsonResponse({'rollNumber': student['RN'], 'name': student['Fname']})
        else:
            print("No student found for Roll Number:", roll_number)
            return JsonResponse({'error': 'Student not found for the provided roll number'}, status=404)
    else:
        print("Roll number parameter is required")
        return JsonResponse({'error': 'Roll number parameter is required'}, status=400)
    
 

@login_required
def save_table_data(request):
    if request.method == 'POST':
        # Access form-encoded POST data directly
        roll_number = request.POST.get('rollNumber')
        name = request.POST.get('name')
        print("Received Roll Number:", roll_number) 
        print("Received name:", name) 
        current_user = request.user
        
        if roll_number and name and current_user:
        # if roll_number and name:
            # Check if the student with the provided roll number already exists
            if not Student.objects.filter(roll_number=roll_number, user=current_user).exists():
            # if not Student.objects.filter(roll_number=roll_number).exists():
                # If the student does not exist, create a new Student object and save it to the database
                student = Student(roll_number=roll_number, name=name, user=current_user)
                # student = Student(roll_number=roll_number, name=name)
                student.save()
                # return messages.success("Student data saved successfully.!")
                messages.success(request, "Student data saved successfully.!")
                
                # return JsonResponse({'message': 'Student data saved successfully.'})
            else:
                # return messages.error("Student with the provided roll number already exists.!")
                messages.error(request, "Student with the provided roll number already exists.!")                
                # return JsonResponse({'error': 'Student with the provided roll number already exists.'}, status=400)
        else:
            # return messages.error("Roll number and name are required fields.!")
            messages.error(request, "Roll number and name are required fields.")   
            # return JsonResponse({'error': 'Roll number and name are required fields.'}, status=400)
    else:
        # return messages.error("Only POST requests are allowed.!")
        messages.error(request, "Only POST requests are allowed.")
        # return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    return redirect('homesM')
    
    
    
def delete_student(request):
    if request.method == 'POST':
        roll_number = request.POST.get('rollNumber')
        print("Received Roll Number:", roll_number) 
        
        if roll_number:
            try:
                # Try to get the student with the provided roll number
                student = Student.objects.get(roll_number=roll_number)
                # If the student exists, delete it
                student.delete()
                messages.success(request, 'Student data deleted successfully.')
            except Student.DoesNotExist:
                # If the student with the provided roll number does not exist
                messages.error(request, 'Student with the provided roll number does not exist.')
        else:
            # If roll number is not provided in the request
            messages.error(request, 'Roll number parameter is required.')
            # return HttpResponseBadRequest()
    else:
        # If request method is not POST
        messages.error(request, 'Only POST requests are allowed.')
        # return HttpResponseNotAllowed(['POST'])

    return redirect('homesM')  # Redirect to the home page after deletion    
    
    
    
# def display_student_data(request):
#     # Retrieve data associated with the current user
#     current_user = request.user
#     student_data = Student.objects.filter(user=current_user)

#     # Pass the filtered data to the template for rendering
#     return render(request, 'homeM.html', {'student_data': student_data})    

# def upload_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         # Handle image upload
#         image = request.FILES['image']
#         # Save the image to a location on the server
#         # Replace 'path/to/save/image.jpg' with the actual path
#         with open('path/to/save/image.jpg', 'wb+') as destination:
#             for chunk in image.chunks():
#                 destination.write(chunk)
#         # Return the URL of the saved image (you'll need to determine this URL based on your server setup)
#         image_url = '/path/to/saved/image.jpg'
#         return render(request, 'printr.html', {'image_url': image_url})
#     return render(request, 'printr.html')


# def nameM(request):
#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         # Get the user's ID
#         user_id = request.user.username
        
#         # Print the user ID for debugging
#         print("User ID:", user_id)
        
#         try:
#             # Fetch the corresponding name from the pdm table
#             user_info = pdmM.objects.get(IDM=user_id)
#             user_name = user_info.FnameM
            
#             # Print the user name for debugging
#             print("User Name:", user_name)
#         except pdmM.DoesNotExist:
#             # Handle the case where user information is not found
#             user_name = "Unknown"
#             print("User information not found")
#     else:
#         # User is not authenticated, handle accordingly
#         user_name = "Guest"
    
#     # Pass the username to the template context
#     return render(request, 'baseM.html', {'user_name': user_name})


# @login_required
# def user_info(request):
#     user_info = None
#     if request.user.is_authenticated:
#         current_user_id = request.user.id
#         try:
#             user_info = pdmM.objects.get(IDM=current_user_id)
#         except pdmM.DoesNotExist:
#             pass
#     return {'user_info': user_info}

# @login_required
# def my_view(request):
#     current_user_id = request.user.id
#     try:
#         pdm_user = pdmM.objects.get(IDM=current_user_id)
#     except pdmM.DoesNotExist:
#         pdm_user = None
#     return render(request, 'baseM.html', {'pdm_user': pdm_user})


# def search_student(request):
#     if request.method == 'GET' and 'roll_number' in request.GET:
#         roll_number = request.GET.get('roll_number')
#         student = pdM.objects.filter(RN=roll_number).first()
#         if student:
#             return render(request, 'home.html', {'student': student})
#         else:
#             # Handle case where student with provided roll number is not found
#             return render(request, 'home.html', {'error_message': 'Student not found'})
#     return render(request, 'home.html')

# def fetch(request):
    # fetchdata = pdM.objects.all()
    # return render(request, 'home/homes.html', {'fetchdata': fetchdata})