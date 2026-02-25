from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Admin/Anonymous/home.html')

def signup(request):
    return render(request, 'Admin/Anonymous/signup.html')

def login(request):
    return render(request, 'Admin/Anonymous/login.html')

def dashboard(request):
    return render(request, 'Admin/MAdmin/dashboard.html')

def profile(request):
    return render(request, 'Admin/MAdmin/profile.html')

def add(request):
    return render(request, 'Admin/MAdmin/add.html')

def manage(request):
    return render(request, 'Admin/MAdmin/manage.html')

def OAdashboard(request):
    return render(request, 'Admin/OpAdmin/dashboard.html')

def OAprofile(request):
    return render(request, 'Admin/OpAdmin/profile.html')

def doctoradd(request):
    return render(request, 'Admin/OpAdmin/doctor/add.html')

def doctormanage(request):
    return render(request, 'Admin/OpAdmin/doctor/manage.html')

def helperadd(request):
    return render(request, 'Admin/OpAdmin/helper/add.html')

def helpermanage(request):
    return render(request, 'Admin/OpAdmin/helper/manage.html')

def receptionistadd(request):
    return render(request, 'Admin/OpAdmin/receptionist/add.html')    

def receptionistmanage(request):
    return render(request, 'Admin/OpAdmin/receptionist/manage.html')
