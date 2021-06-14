from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from datetime import date
from .filters import *


@unauthenticated_user
def index(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = Success_Story.objects.all()[:3]
    context = {'tpo': tpo, 'studupdate': studupdate, 'form': form}
    return render(request, 'index.html', context)


# def basic(request):
#     tpo_update = Tpo_Update.objects.all()
#     studupdate = Student_Update.objects.all()
#     context = {'tpo_update': tpo_update, 'studupdate': studupdate}
#     return render(request, 'basic.html', context)


# users testing
@unauthenticated_user
def register(request):
    tpo_update = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            enroll = form.cleaned_data.get('enrollment')
            print("---------------------------", enroll)
            username = form.cleaned_data.get('username')
            group2 = Group.objects.get(name='company')
            group1 = Group.objects.get(name='student')
            if enroll == 'student':
                user.groups.add(group1)
                Student.objects.create(
                    user=user,
                    name=username,
                )

                messages.success(request, 'student accounts was created for ' + username)
                return redirect('login')
            else:
                user.groups.add(group2)
                Company.objects.create(
                    user=user,
                    name=user.username,
                )

                messages.success(request, 'company accounts was created for ' + username)
                return redirect('login')
    else:
        context = {'tpo': tpo_update, 'studupdate': studupdate, 'form': form}
        return render(request, 'student_register.html', context)


@unauthenticated_user
def loginview(request):
    tpo_update = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        request.session['loginname'] = username
        print("----------------session set successfully---------------")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {'tpo': tpo_update, 'studupdate': studupdate}
    return render(request, 'student_login.html', context)


def logoutview(request):
    tpo = Tpo_Update.objects.all()
    context = {'tpo': tpo}
    try:
        del request.session['loginname']
    except KeyError:
        pass
    logout(request)
    return redirect("index")


# account profiles


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def SaccountSettings(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    if request.user.student:
        student = request.user.student
        form = StudentForms(instance=student)
        if request.method == 'POST':
            form = StudentForms(request.POST, request.FILES, instance=student)
            if form.is_valid():
                form.save()
    context = {'form': form, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'account_settings.html', context)


# student views
# user page

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student(request):
    str1 = "Welcome,Patel Bhavin"
    tpo = Tpo_Update.objects.all()
    print("records is:", tpo.count())
    context = {'tpo': tpo, 'str1': str1}
    return render(request, 'student.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_dashboard(request):
    totalapply = Applied_Student.objects.all().count()
    tpo = Tpo_Update.objects.all()
    vacancy = Add_vaccancy.objects.all()
    vacancy_no = Add_vaccancy.objects.all().count()
    studupdate = Student_Update.objects.all()
    applied_job = Applied_Student.objects.all().count()
    context = {'tpo': tpo, 'totalapply': totalapply, 'vacancy': vacancy, 'studupdate': studupdate,
               'applied_job': applied_job, 'vacancy_no': vacancy_no}
    return render(request, 'student_dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_form(request):
    tpo = Tpo_Update.objects.all()
    upload = StudentForm()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'form': upload, 'studupdate': studupdate}
    if request.method == 'POST':
        upload = StudentForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_dashboard')
        else:
            return HttpResponse(
                """your form is wrong, reload on <a href = "{{ url : 'student_dashboard'}}">reload</a>""")
    else:
        return render(request, 'student_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def view_student_form(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    username = request.session.get('loginname')
    print("-----------username------", username)
    studentform = Student_Form.objects.filter(s_name=username)
    context = {'studentform': studentform, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'view_student_form.html', context)


def update_student_form(request, book_id):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    book_id = int(book_id)
    try:
        book_sel = Student_Form.objects.get(id=book_id)
    except Student_Form.DoesNotExist:
        return redirect('student_dashboard')
    book_form = StudentForm(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('student_dashboard')
    context = {'form': book_form, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'student_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def view_vaccancy(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = Add_vaccancy.objects.all()
    # myFilter = studentlistfilters(request.GET, queryset=form)
    # selected_student_list = myFilter.qs
    user_list = Add_vaccancy.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'form': form, 'tpo': tpo, 'studupdate': studupdate, 'users': users}
    return render(request, 'view_vacancy.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def view_vaccancy_details(request, myid):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    current_date = date.today()
    print("-----------------------", current_date)
    if request.method == 'POST':
        upload = ApplyJobForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_dashboard')
        else:
            return HttpResponse(
                """your form is wrong, reload on <a href = "{{ url : 'student_dashboard'}}">reload</a>""")
    else:
        tpo = Tpo_Update.objects.all()
        form = Add_vaccancy.objects.filter(id=myid)
        jobform = ApplyJobForm()
        context = {'form': form, 'tpo': tpo, 'jobform': jobform, 'studupdate': studupdate, 'current_date': current_date}
        return render(request, 'view_vacancy_details.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def applied_job_list(request):
    applied_job = Applied_Student.objects.all()
    company_details = Add_vaccancy.objects.all()
    context = {'applied_job': applied_job, 'company_details': company_details}
    return render(request, 'applied_job_list.html', context)


# -------------------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['student', 'company', 'admin'])
def selected_student_list(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()

    selected_student_list = Selected_Students.objects.all()
    myFilter = studentlistfilters(request.GET, queryset=selected_student_list)
    selected_student_list = myFilter.qs
    user_list = Selected_Students.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'tpo': tpo, 'studupdate': studupdate, 'users': users, 'myFilter': myFilter}
    return render(request, 'selected_student_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_selected_student(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    Selected_Students.objects.all().delete()
    print("Selected Student Database Cleared..........")
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'selected_student_list.html', context)


# ----------------------------------------------------------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def student_profile(request):
    tpo = Tpo_Update.objects.all()
    request.session['name'] = 'Bhavin Patel'
    studname = request.session['name']
    profile_data = Student_Form.objects.filter(s_name=studname)
    print(profile_data)
    context = {'student_profile': profile_data, 'tpo': tpo}
    return render(request, 'student_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def successStory(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    upload = SuceessStoryForm()
    username = request.session.get('loginname')
    if request.method == 'POST':
        upload = SuceessStoryForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_dashboard')
        else:
            messages.warning(request, 'YOU ENTERED A WRONG INFO.')
            return redirect('successStory')
    else:

        context = {'tpo': tpo, 'studupdate': studupdate, 'form': upload, 'username': username}
        return render(request, 'successStory.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['student'])
def view_successStory(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = Success_Story.objects.all()
    username = request.session.get('loginname')
    user_list = Success_Story.objects.all()
    page = request.GET.get('page', 1)
    page_entries = 3
    paginator = Paginator(user_list, page_entries)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'tpo': tpo, 'studupdate': studupdate, 'users': users, 'username': username, 'page_entries': page_entries}
    return render(request, 'view_successStory.html', context)


# company views


def company(request):
    tpo = Tpo_Update.objects.all()
    context = {'tpo': tpo}
    return render(request, 'company.html', context)


def company_register(request):
    tpo = Tpo_Update.objects.all()
    return render(request, "index.html")


@login_required(login_url='login')
@allowed_users(allowed_roles=['company'])
def company_dashboard(request):
    tpo = Tpo_Update.objects.all()
    vacancy = Add_vaccancy.objects.all()
    studupdate = Student_Update.objects.all()
    applied_stud = Applied_Student.objects.all().count()
    selected_stud = Selected_Students.objects.all().count()
    context = {'tpo': tpo, 'vacancy': vacancy, 'studupdate': studupdate, 'applied_stud': applied_stud,
               'selected_stud': selected_stud}
    # return HttpResponseRedirect(reverse('company_dashboard'))
    return render(request, 'company_dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['company'])
def CaccountSettings(request):
    if request.user.company:
        company = request.user.company
        form = CompanyForm(instance=company)
        if request.method == 'POST':
            form = CompanyForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()

    context = {'form': form}
    return render(request, 'account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['company', 'admin'])
def view_apply_student_list(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    company = Add_vaccancy.objects.all()
    user_list = Applied_Student.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'tpo': tpo, 'companydetails': company, 'studupdate': studupdate, 'users': users}
    return render(request, 'view_apply_student_list.html', context)


def add_selected_student(request):
    tpo = Tpo_Update.objects.all()
    context = {'tpo': tpo}
    if request.method == "POST":
        enrollment = request.POST.get('enrollment', '')
        name = request.POST.get('name', '')
        mobile = request.POST.get('mobile', '')
        branch = request.POST.get('branch', '')
        selected = request.POST.get('selected', '')
        Selected_Students(enrollment=enrollment, name=name, mobile=mobile, branch=branch, selected=selected).save();
        print(name, " is selected")
        return HttpResponseRedirect(reverse("add_selected_student"))
    else:
        return render(request, 'add_selected_student.html', context)


def add_vacancy(request):
    tpo = Tpo_Update.objects.all()
    upload = VaccancyForm()
    context = {'tpo': tpo, 'form': upload}
    if request.method == 'POST':
        upload = VaccancyForm(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('company_dashboard')
        else:
            return HttpResponse(
                """your form is wrong, reload on <a href = "{{ url : 'company_dashboard'}}">reload</a>""")
    else:
        return render(request, 'add_vacancy.html', context)


def view_company_vacancy(request):
    tpo = Tpo_Update.objects.all()
    username = request.session.get('loginname')
    form = Add_vaccancy.objects.filter(name=username)
    studupdate = Student_Update.objects.all()
    context = {'form': form, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'view_company_vacancy.html', context)


def update_vacancy(request, book_id):
    studupdate = Student_Update.objects.all()
    book_id = int(book_id)
    try:
        book_sel = Add_vaccancy.objects.get(id=book_id)
    except Add_vaccancy.DoesNotExist:
        return redirect('company_dashboard')
    book_form = VaccancyForm(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('company_dashboard')
    context = {'form': book_form, 'studupdate': studupdate}
    return render(request, 'add_vacancy.html', context)


# admin views


@login_required(login_url='login')
@admin_only
def admin(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'admin.html', context)


@login_required(login_url='login')
@admin_only
def admin_dashboard(request):
    tpo = Tpo_Update.objects.all()
    vacancy = Add_vaccancy.objects.all()
    studupdate = Student_Update.objects.all()
    totalapply = Applied_Student.objects.all().count()
    totalplaced = Selected_Students.objects.all().count()
    stud_no = Student.objects.all().count()
    comp_no = Company.objects.all().count()
    context = {'tpo': tpo, 'totalapply': totalapply, 'studupdate': studupdate,
               'vacancy': vacancy, 'stud_no': stud_no, 'comp_no': comp_no, 'totalplaced': totalplaced}
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login')
@admin_only
def manage_tpo_update(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    if request.method == "POST":
        tpo_update = request.POST.get('tpo_update', '')
        Tpo_Update(tpo_update=tpo_update).save();
        return HttpResponseRedirect(reverse("manage_tpo_update"))
    else:
        return render(request, 'manage_tpo_update.html', context)


@login_required(login_url='login')
@admin_only
def view_tpo_update(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'view_tpo_update.html', context)


@login_required(login_url='login')
@admin_only
def delete_tpo_update(request, myid):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    myid = int(myid)
    try:
        deleteupdate = Tpo_Update.objects.get(id=myid)
    except Tpo_Update.DoesNotExist:
        return redirect('admin_dashboard')
    deleteupdate.delete()
    return render(request, 'view_tpo_update.html', context)


@login_required(login_url='login')
@admin_only
def manage_student_update(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    if request.method == "POST":

        student_update = request.POST.get('student_update', '')
        Student_Update(student_update=student_update).save();
        return HttpResponseRedirect(reverse("manage_student_update"))
    else:
        return render(request, 'manage_student_update.html', context)


@login_required(login_url='login')
@admin_only
def view_student_update(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'view_student_update.html', context)


@login_required(login_url='login')
@admin_only
def delete_student_form(request, book_id):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}

    book_id = int(book_id)
    try:
        book_sel = Student_Form.objects.get(id=book_id)
    except Student_Form.DoesNotExist:
        return redirect('admin_dashboard')
    book_sel.delete()
    return redirect('admin_dashboard')


@login_required(login_url='login')
@admin_only
def delete_student_update(request, myid):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    myid = int(myid)
    try:
        deleteupdate = Student_Update.objects.get(id=myid)
    except Tpo_Update.DoesNotExist:
        return redirect('admin_dashboard')
    deleteupdate.delete()
    return render(request, 'view_student_update.html', context)


@login_required(login_url='login')
@admin_only
def delete_vacancy(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Add_vaccancy.objects.get(id=book_id)
    except Add_vaccancy.DoesNotExist:
        return redirect('admin_dashboard')
    book_sel.delete()
    return redirect('admin_dashboard')


# User Accounts Register Data


@login_required(login_url='login')
@admin_only
def new_students_register(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    student_register = Student.objects.all()
    user_list = Student.objects.all()
    page = request.GET.get('page', 1)
    page_entries = 5
    paginator = Paginator(user_list, page_entries)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'tpo': tpo, 'studupdate': studupdate, 'student_register': student_register, 'users': users,
               'page_entries': page_entries}
    return render(request, 'new_students_register.html', context)


@login_required(login_url='login')
@admin_only
def new_company_register(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    company_register = Company.objects.all()
    user_list = Company.objects.all()
    page = request.GET.get('page', 1)
    page_entries = 5
    paginator = Paginator(user_list, page_entries)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(page_entries)
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'company_register': company_register, 'tpo': tpo, 'studupdate': studupdate, 'users': users,
               'page_entries': page_entries}
    return render(request, 'new_company_register.html', context)


@login_required(login_url='login')
@admin_only
def view_list_student_form(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    student_form = Student_Form.objects.all()
    user_list = Student_Form.objects.all()
    page = request.GET.get('page', 1)
    page_entries = 5
    paginator = Paginator(user_list, page_entries)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'student_form': student_form, 'tpo': tpo, 'studupdate': studupdate, 'users': users,
               'page_entries': page_entries}
    return render(request, 'view_list_student_form.html', context)


@login_required(login_url='login')
@admin_only
def admin_view_vacancy(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = Add_vaccancy.objects.all()
    context = {'form': form, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'admin_view_vacancy.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_apply_student_list(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    Applied_Student.objects.all().delete()
    print("Selected Student Database Cleared..........")
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'view_apply_student_list.html', context)


@login_required(login_url='login')
@admin_only
def admin_view_vacancy_details(request, myid):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    form = Add_vaccancy.objects.filter(id=myid)
    context = {'form': form, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'admin_view_vacancy_details.html', context)


# Search for all data Access

def search(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    query = request.GET['query']
    print('---------------------------------', query)
    if ('query' in request.GET) and request.GET['query'].strip():
        query_string = request.GET.get('query')
        studlist = Selected_Students.objects.filter(name__icontains=query_string)
    else:
        studlist = None
    # studlist = Selected_Students.objects.filter(name__icontains=query, enrollment_icontains=query)
    print('------------------------', studlist)
    context = {'studlist': studlist, 'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'search.html', context)


def contactus(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'contactus.html', context)


def aboutus(request):
    tpo = Tpo_Update.objects.all()
    studupdate = Student_Update.objects.all()
    context = {'tpo': tpo, 'studupdate': studupdate}
    return render(request, 'aboutus.html', context)
