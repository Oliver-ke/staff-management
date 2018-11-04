from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required

from .forms import A_staff_Form, None_A_staff_Form, searchForm, RegisterForm
from .models import A_staff, None_A_staff
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from fnmatch import filter


#controller route to home page/index page
@login_required(login_url = '')
def index(request):
    if request.user.is_authenticated:
        form = searchForm()
        print(request.user)
        context = {
            'form' : form
        }
        return render(request, 'school_management/index.html', context)
    else:
        redirect('login')

#controller route to staff's page for only academic staffs 
def addForm(request):
    if request.method == 'POST':
        form = A_staff_Form(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            name = form.cleaned_data['name']
            dFirstAppointment = form.cleaned_data['dFirstAppointment']
            rank = form.cleaned_data['rank']
            qualification = form.cleaned_data['qualification']
            salaryGLevel = form.cleaned_data['salaryGLevel']
            step = form.cleaned_data['step']
            yLastPromotion = form.cleaned_data['yLastPromotion']
            pressentYear = form.cleaned_data['pressentYear']
            teachingE = form.cleaned_data['teachingE']
            publicationS = form.cleaned_data['publicationS']
            responsibilityS = form.cleaned_data['responsibilityS']

            avater = form.cleaned_data['avater']
            pub = form.cleaned_data['pub']
            faculty = form.cleaned_data['faculty']

            ##controller calculated values
            Tscore = teachingE + publicationS + responsibilityS
            pressentYear, yLastPromotion = (pressentYear, yLastPromotion) if pressentYear > yLastPromotion else (yLastPromotion, pressentYear)
            difference_in_years = relativedelta(pressentYear, yLastPromotion).years
            new_lec = A_staff(
                name=name,
                dFirstAppointment=dFirstAppointment,
                rank=rank,
                qualification=qualification,
                salaryGLevel=salaryGLevel,
                step=step,
                yLastPromotion=yLastPromotion,
                pressentYear=pressentYear,
                teachingE=teachingE,
                publicationS=publicationS,
                responsibilityS=responsibilityS,
                avater=avater,
                pub=pub,
                faculty = faculty,
                totalScore=Tscore,
                duePromotion=True,
                systemRecomUpgrade='yes',
                nYearsPresentG=difference_in_years,
            )
            print(new_lec)
            new_lec.save();
            return redirect('index')
            
        else:
            print('form not valid')
    else:
        form = A_staff_Form()
    context = {'form': form}
    return render(request, 'school_management/form.html',context)

#controller route to the staff's table where all academic staffs in the db are displayed
def staff(request):
    # staffs = A_staff.objects.all()[:10]
    staffs = A_staff.objects.order_by('id')
    context = {
        "staffs": staffs,
        "title": 'Database Records for Academc Staffs',
        
    }
    return render(request, 'school_management/spreadsheet.html', context)

#for search on post
def search(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            staffs = A_staff.objects.filter(name__icontains=name)
            #impliment order_by to arrange content of search by id
            title = 'Staff Database Search Result'
            if not staffs:
                title = 'No Staff in the Database with the Search Querry'
            context = {
                'staffs': staffs,
                'title': title
            }
            return render(request, 'school_management/spreadsheet.html', context)
    else:
        form = searchForm()
    context = {
        'form' : form
    }

    return render(request, 'school_management/index.html', context)

#controller route to the add staff's page for only none academic staffs 
def n_addForm(request):
    if request.method == 'POST':
        form = None_A_staff_Form(request.POST)
        if form.is_valid():
            print('form is valid')
            name = form.cleaned_data['name']
            dFirstAppointment = form.cleaned_data['dFirstAppointment']
            a_pcRecom = form.cleaned_data['rank']
            qualification = form.cleaned_data['qualification']
            salaryGLevel = form.cleaned_data['salaryGLevel']
            step = form.cleaned_data['step']
            yLastPromotion = form.cleaned_data['yLastPromotion']
            pressentYear = form.cleaned_data['pressentYear']
            responsibilityS = form.cleaned_data['responsibilityS']

            ##controller calculated values
            Tscore =  responsibilityS  #need work #
            pressentYear, yLastPromotion = (pressentYear, yLastPromotion) if pressentYear > yLastPromotion else (yLastPromotion, pressentYear)
            difference_in_years = relativedelta(pressentYear, yLastPromotion).years
            new_staff = None_A_staff(
                name=name,
                dFirstAppointment=dFirstAppointment,
                a_pcRecom=a_pcRecom,
                qualification=qualification,
                salaryGLevel=salaryGLevel,
                step=step,
                yLastPromotion=yLastPromotion,
                pressentYear=pressentYear,
                responsibilityS=responsibilityS,
                totalScore=Tscore,
                duePromotion=True,
                systemRecomUpgrade='yes',
                nYearsPresentG=difference_in_years,
            )
            print(new_staff)
            new_staff.save();
            return redirect('Nstaffs')
            
        else:
            print('form not valid')
    else:
        form = None_A_staff_Form()
    context = {'form': form}
    return render(request, 'school_management/form2.html',context)

#controller route to the staff's table where all none academic staffs in the db are displayed
def n_staff(request):
    staffs = None_A_staff.objects.all()
    context = {
        "staffs" : staffs
    }
    return render(request, 'school_management/spreadsheet2.html', context)
#this route is used to display staff's profile
def profile(request, staffs_id):
    print(request)
    staff = A_staff.objects.get(pk=staffs_id)
    context = {'staff' : staff}
    return render(request, 'school_management/profile.html', context)

#for staff registration
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'school_management/register.html'
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['user_name']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Passwords do not match.'
                })

            elif form.cleaned_data['password'].isdigit():
                return render(request, template, {
                    'form': form, 
                    'error_message': ' password contains all digits, please use a mixture of digit and letters'
                })
            else:
                # Create the user: 
                user = User.objects.create_user(
                    form.cleaned_data['user_name'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
                user.full_name = form.cleaned_data['full_name']
                # user.last_name = form.cleaned_data['last_name']
                # user.phone_number = form.cleaned_data['phone_number']
                user.save()
                
                # Login the user
                login(request, user)
                
                # redirect to accounts page:
                # return HttpResponseRedirect('/post/index2')
                context = {'user': user}
                return render(request, 'school_management/index.html', context)
        else:
            print('form has error')
   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
        print('request is not a post request')

    return render(request, template, {'form': form})
    
#for staff login
def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        # username = request.POST['user']
        # password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            form = searchForm()
            # Success, now let's login the user. 
            context = {'form': form}
            return render(request, 'school_management/index.html', context)
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'school_management/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'school_management/login.html')

