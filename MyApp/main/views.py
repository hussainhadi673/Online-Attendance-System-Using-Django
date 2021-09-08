from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileUpdateForm,UserUpdateForm, EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime
from .models import *



def home(request):
    return render(request, 'main/home.html')

def base(request):
    return render(request, 'main/base.html')

def base_test(request):
    return render(request, 'main/base_test.html')



def student_portal(request):
    return render(request, 'main/student_portal.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {'form': form})

user = ""
@login_required(login_url='login')
def student_dashboard(request):
    return render(request, 'main/student_dashboard.html')

def loginPage(request):
    global user
    if request.user.is_authenticated:
        pass
        #return redirect('admin_dashboard')
    #else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def s_attendance(request):
    user = request.user
    today1 = date.today()
    d2 = today1.strftime("%Y-%m-%d")
    d2 = datetime.strptime(d2, '%Y-%m-%d')
    print(d2)

    queryset2 = Employees.object.all()
    check1 = 0
    for i in queryset2:
        if str(i.username1) == str(user):
            check1 += 1
    print(check1)
    if check1 == 0:
        if request.method == "POST":
            fname = request.POST.get('fname')
            attendance = request.POST.get('attendance')
            today = date.today()
            d1 = today.strftime("%Y-%m-%d")
            if attendance == 'on':
                attendance = 'Present'
            else:
                attendance = 'Absent'

            messages.info(request, f'Confirm your are {attendance}, You wont be able to change it')
            query1 = Employees.object.all()
            for k in query1:
                pass
            print(d1)
            ins = Employees(name1=fname, username1=request.user, date1=d1, attendance2=attendance)
            ins.save()
            return redirect('student_dashboard')
    else:
        a3 = 0
        check5 = 0
        for i in queryset2:
            if str(i.username1) == str(user):
                a3 = datetime.strptime(i.date1, '%Y-%m-%d')
                if d2 == a3:
                    check5 = 1

        #a3 = str(a2[-1].date1)
        #if int(d2[0:2]) - int(a3[0:2])  != 0:
        if check5 == 0:
            if request.method == "POST":
                fname = request.POST.get('fname')
                attendance = request.POST.get('attendance')
                today = date.today()
                d1 = today.strftime("%Y-%m-%d")
                d1= str(d1)
                if attendance == 'on':
                    attendance = 'Present'
                else:
                    attendance= 'Absent'

                messages.info(request, f'Confirm your are {attendance}, You wont be able to change it')
                ins = Employees(name1=fname, username1=request.user, date1=d1, attendance2=attendance)
                ins.save()
                return redirect('student_dashboard')
        else:
            messages.info(request, 'You have already market your attendence for today')
            return redirect('student_dashboard')
    return render(request, 'main/s_attendance.html')


@login_required(login_url='login')
def student_view(request):

    queryset = Employees.object.all()
    context = {}
    a=[]
    for i in queryset:
        if str(i.username1) == str(request.user):
            a.append(i)

    context = {'queryset': a,}
    return render(request, 'main/student_view.html', context)

def main(request):
    return render(request, 'main/main.html')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        #u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            print("yess")
            #u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        #u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        #'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'main/profile.html', context)

@login_required(login_url='login')
def leave_attendance(request):
    global user
    if request.method == "POST":
        name2 = request.POST.get('firstname')
        date2 = request.POST.get('leave')
        concern = request.POST.get('subject')
        messages.info(request, f'Leave Request Sent')
        ins1 = Leave_Request(name2=name2, username2=request.user, date2=date2, concern=concern)
        ins1.save()
        return redirect('student_dashboard')
    return render(request, 'main/leave_attendance.html')


def admin_login(request):
    global user
    if request.user.is_authenticated:
        pass
        # return redirect('admin_dashboard')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user.is_staff)
            if user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'main/admin_login.html', context)

@login_required(login_url='admin_login')
def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')

@login_required(login_url='admin_login')
def admin_attendance_view(request):
    queryset = Employees.object.all()
    check2=1

    context = {

        'queryset': queryset}
    return render(request, 'main/admin_attendance_view.html', context)

@login_required(login_url='admin_login')
def edit(request, id):
    print(id)
    queryset = Employees.object.filter(id=id)

    attendance = str(queryset[0].attendance2)

    context = {'name': queryset[0].name1,
               'username': queryset[0].username1,
               'date': queryset[0].date1,
               'attendance': attendance,
                }

    item = get_object_or_404(Employees, id=id)

    if request.method == "POST":
        fname = request.POST.get('fname')
        username =  request.POST.get('username')
        date = request.POST.get('date')
        attendance = request.POST.get('attendance')
        Employees.object.filter(id=id).update(name1= fname, username1= username, date1=date,
                                              attendance2=attendance)
        return redirect('admin_attendance_view')

    return render(request, 'main/edit.html', context)

@login_required(login_url='admin_login')
def delete(request,id):
    Employees.object.filter(id=id).delete()
    return redirect('admin_attendance_view')

@login_required(login_url='admin_login')
def admin_mark_atten(request):
    global user
    query = Employees.object.all()
    j=0
    for j in query:
        pass
    if request.method == "POST":
        fname_1 = request.POST.get('fname')
        username_1 = request.POST.get('username')
        date_1 = request.POST.get('date')
        attendance_1 = request.POST.get('attendance')
        if j == 0:
            ins=Employees(id=j+1,name1=fname_1, username1=username_1, date1=str(date_1),
                                              attendance2=attendance_1)
        else:
            ins=Employees(id=j.id+1,name1=fname_1, username1=username_1, date1=str(date_1),
                                              attendance2=attendance_1)
        ins.save()
        return redirect('admin_mark_atten')
    return render(request, 'main/admin_mark_atten.html')

@login_required(login_url='admin_login')
def from_to(request):

    a=Employees.object.values('username1').distinct()
    default = []
    for z in range(len(a)):
        default.append( a[z]['username1'] )
    context = { 'initial' : default}

    if request.method == "POST":
        user3 = request.POST.get('name')
        f_date = request.POST.get('fdate')
        to_date = request.POST.get('tdate')
        if f_date != "":
            f_date = datetime.strptime(f_date, '%Y-%m-%d')
        if to_date != "":
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
        print(f_date)
        user3 = str(user3)
        query4 = Employees.object.all()
        user2 = 'All'
        for z in range(len(a)):
            if user3 == a[z]['username1']:
                user2 = user3
        if f_date == "" and to_date == "":
            if user2 == 'All':
                queryset5 = Employees.object.all()
                context = {'initial': default,
                           'query': queryset5}

            else:
                queryset5 = Employees.object.filter(username1=user2)
                context = {'initial': default,
                    'query' : queryset5}

        if f_date == "" and to_date != "":
            if user3 == 'All':
                queryset5 = Employees.object.all()
            else:
                queryset5 = Employees.object.filter(username1=user2)
            query5 = []
            for x in queryset5:
                date_time_obj = datetime.strptime(x.date1, '%Y-%m-%d')
                #to_date = datetime.strptime(to_date, '%Y-%m-%d')
                if ( date_time_obj > to_date ):
                    pass
                else:
                    query5.append(x)

                context = {'initial': default,
                           'query': query5}

        if f_date != "" and to_date == "":
            if user3 == 'All':
                queryset5 = Employees.object.all()
            else:
                queryset5 = Employees.object.filter(username1=user2)
            query5 = []
            for x in queryset5:
                date_time_obj = datetime.strptime(x.date1, '%Y-%m-%d')
                #f_date = datetime.strptime(f_date, '%Y-%m-%d')
                #print(date_time_obj < f_date)
                if (date_time_obj < f_date):
                    pass
                else:
                    query5.append(x)

                context = {'initial': default,
                           'query': query5}
        if f_date != "" and to_date != "":
            if user3 == 'All':
                queryset5 = Employees.object.all()
            else:
                queryset5 = Employees.object.filter(username1=user2)
            query5 = []
            for x in queryset5:
                date_time_obj = datetime.strptime(x.date1, '%Y-%m-%d')
                #to_date = datetime.strptime(to_date, '%Y-%m-%d')
                #f_date = datetime.strptime(f_date, '%Y-%m-%d')

                if (date_time_obj < f_date) or (date_time_obj > to_date ):
                    pass
                else:
                    query5.append(x)

                context = {'initial': default,
                           'query': query5}
    return render(request, 'main/from_to.html', context)

@login_required(login_url='admin_login')
def admin_grade(request):
    present = 0
    absent = 0
    leave = 0
    total = 0
    grade = ''
    context = {}
    leave_query=Leave_Request.objects.all()
    if leave_query != "":
        a = Employees.object.values('username1').distinct()
        default = []
        for z in range(len(a)):
            default.append(a[z]['username1'])
        context = {'initial': default, 'leave_query': leave_query}
    if request.method == "POST":
        guy = request.POST.get('name')
        queryset6 = Employees.object.filter(username1=guy)
        for g in queryset6:
            if g.attendance2 == 'Present':
                present += 1
            elif g.attendance2 == 'Absent':
                absent += 1
            elif g.attendance2 == 'Leave':
                leave += 1
            total += 1
            present_percent = (present/total)*100
            if present > 26:
                grade = 'A'
            elif present >= 20 and present < 26:
                grade = 'B'
            elif present >= 11 and present < 19:
                grade = 'C'
            else:
                grade = 'D'

        try:
            context = {'initial': default, 'leave_query': leave_query, 'present': present, 'absent': absent, 'leave': leave, 'percent': int(present_percent), 'grade': grade}
        except:
            context = {}


    return render(request, 'main/admin_grade.html', context)

def admin_base(request):
    return render(request, 'main/admin_base.html')

# Create your views here.



