from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from myapp.models import Donor_form
from datetime import datetime

# Create your views here.
def index(request):
   
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicespage")

def login(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')

def guidelines(request):
    return render(request,'guidelines.html')


def donor_form(request):
    if request.method == "POST":
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        district = request.POST.get('district')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        contact_no = request.POST.get('contact_no')
        size = request.POST.get('size')
        quantity = request.POST.get('quantity')
        date_s = request.POST.get('date_s')
        time = request.POST.get('time')
        e_img = request.POST.get('e_img')
        donor_form = Donor_form(email=email, address1=address1, address2=address2, district=district ,city=city ,state=state ,pincode=pincode ,contact_no=contact_no ,size=size ,quantity=quantity ,date_s=date_s ,time=time, e_img=e_img, date=datetime.today())  
        donor_form.save()
    return render(request,'donor_form.html')

def dashboard(request):
        return render(request,'dashboard.html')
