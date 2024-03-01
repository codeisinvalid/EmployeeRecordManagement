from django.shortcuts import render,redirect 
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method =="POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        pwd = request.POST['password']
        ec = request.POST['empcode']

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)

            EmployeeDetail.objects.create(user = user, empcode = ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)

            error = "no"

        except:
            error = "yes"

    return render(request, 'registration.html', locals())

def emp_login(request):
    error=""
    if request.method=="POST":
        u = request.POST['emailid']
        p = request.POST['password']

        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error="no"
        else:
            error="yes"

    return render(request, 'emp_login.html',locals())


def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'emp_home.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)

    if request.method =="POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        ec = request.POST['empcode']


        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empcode=ec
        employee.designation = designation
        employee.contact =contact
        employee.empdept = dept
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def Logout(request):
    logout(request)
    return redirect('login')


def admin_login(request):

    error=""
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"

    return render(request, 'admin_login.html', locals())


def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request, 'myexperience.html', locals())


def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    if request.method =="POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation = request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name=company1name
        experience.company1designation=company1designation
        experience.company1salary=company1salary
        experience.company1duration = company1duration

        experience.company2name=company2name
        experience.company2designation=company2designation
        experience.company2salary=company2salary
        experience.company2duration = company2duration

        experience.company3name=company3name
        experience.company3designation=company3designation
        experience.company3salary=company3salary
        experience.company3duration = company3duration
        
        try:
            experience.save()  
            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_experience.html', locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    if request.method =="POST":
        course_pg = request.POST['course_pg']
        schoolcollege_pg = request.POST['schoolcollege_pg']
        year_of_passing_pg = request.POST['year_of_passing_pg']
        percentage_pg = request.POST['percentage_pg']

        course_grad = request.POST['course_grad']
        schoolcollege_grad = request.POST['schoolcollege_grad']
        year_of_passing_grad = request.POST['year_of_passing_grad']
        percentage_grad = request.POST['percentage_grad']

        course_hsec = request.POST['course_hsec']
        schoolcollege_hsec = request.POST['schoolcollege_hsec']
        year_of_passing_hsec = request.POST['year_of_passing_hsec']
        percentage_hsec = request.POST['percentage_hsec']

        course_sec = request.POST['course_sec']
        schoolcollege_sec = request.POST['schoolcollege_sec']
        year_of_passing_sec = request.POST['year_of_passing_sec']
        percentage_sec = request.POST['percentage_sec']

        education.course_pg = course_pg
        education.schoolcollege_pg =schoolcollege_pg
        education.year_of_passing_pg=year_of_passing_pg
        education.percentage_pg=percentage_pg

        education.course_grad =course_grad
        education.schoolcollege_grad = schoolcollege_grad
        education.year_of_passing_grad = year_of_passing_grad
        education.percentage_grad = percentage_grad

        education.course_hsec=course_hsec
        education.schoolcollege_hsec = schoolcollege_hsec
        education.year_of_passing_hsec = year_of_passing_hsec
        education.percentage_hsec = percentage_hsec

        education.course_sec = course_sec
        education.schoolcollege_sec=schoolcollege_sec
        education.year_of_passing_sec=year_of_passing_sec
        education.percentage_sec=percentage_sec

        try:
            education.save()  
            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_myeducation.html', locals())

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    error = ""
    user = request.user

    if request.method =="POST":
        c = request.POST['password']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error="not"
        except:
            error = "yes"

    return render(request, 'change_password.html', locals())


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    error = ""
    user = request.user

    if request.method =="POST":
        c = request.POST['password']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"

            else:
                error="not"
        except:
            error = "yes"

    return render(request, 'change_passwordadmin.html', locals())


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    employee = EmployeeDetail.objects.all()
    return render(request, 'all_employee.html',locals())


def edit_profile(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    error = ""
    employee = EmployeeDetail.objects.get(id=pid)

    if request.method =="POST":

        fn = request.POST['firstname']
        ln = request.POST['lastname']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        ec = request.POST['empcode']

        employee.user.first_name=fn
        employee.user.last_name=ln
        employee.empcode=ec
        employee.designation = designation
        employee.contact =contact
        employee.empdept = dept
        employee.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_profile.html', locals())

def edit_education(request, pid):

    if not request.user.is_authenticated:
        return redirect('login')
    error = ""

    user=User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)

    if request.method =="POST":
        course_pg = request.POST['course_pg']
        schoolcollege_pg = request.POST['schoolcollege_pg']
        year_of_passing_pg = request.POST['year_of_passing_pg']
        percentage_pg = request.POST['percentage_pg']

        course_grad = request.POST['course_grad']
        schoolcollege_grad = request.POST['schoolcollege_grad']
        year_of_passing_grad = request.POST['year_of_passing_grad']
        percentage_grad = request.POST['percentage_grad']

        course_hsec = request.POST['course_hsec']
        schoolcollege_hsec = request.POST['schoolcollege_hsec']
        year_of_passing_hsec = request.POST['year_of_passing_hsec']
        percentage_hsec = request.POST['percentage_hsec']

        course_sec = request.POST['course_sec']
        schoolcollege_sec = request.POST['schoolcollege_sec']
        year_of_passing_sec = request.POST['year_of_passing_sec']
        percentage_sec = request.POST['percentage_sec']

        education.course_pg = course_pg
        education.schoolcollege_pg =schoolcollege_pg
        education.year_of_passing_pg=year_of_passing_pg
        education.percentage_pg=percentage_pg

        education.course_grad =course_grad
        education.schoolcollege_grad = schoolcollege_grad
        education.year_of_passing_grad = year_of_passing_grad
        education.percentage_grad = percentage_grad

        education.course_hsec=course_hsec
        education.schoolcollege_hsec = schoolcollege_hsec
        education.year_of_passing_hsec = year_of_passing_hsec
        education.percentage_hsec = percentage_hsec

        education.course_sec = course_sec
        education.schoolcollege_sec=schoolcollege_sec
        education.year_of_passing_sec=year_of_passing_sec
        education.percentage_sec=percentage_sec

        try:
            education.save()  
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_education.html', locals())

def delete_employee(request, pid):
    if not request.user.is_authenticated:
        redirect('admin_home')
    
    employee=User.objects.get(id=pid)
    employee.delete()
    messages.success(request, "The user is deleted")

    return render (request, 'admin_home.html')

def edit_userexperience(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)

    if request.method =="POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation = request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name=company1name
        experience.company1designation=company1designation
        experience.company1salary=company1salary
        experience.company1duration = company1duration

        experience.company2name=company2name
        experience.company2designation=company2designation
        experience.company2salary=company2salary
        experience.company2duration = company2duration

        experience.company3name=company3name
        experience.company3designation=company3designation
        experience.company3salary=company3salary
        experience.company3duration = company3duration
        
        try:
            experience.save()  
            error = "no"
        except:
            error = "yes"

    return render(request, 'edit_userexperience.html', locals())

