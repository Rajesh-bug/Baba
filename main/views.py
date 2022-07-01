import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GotraData, WorkData, Customerdata, SlipData
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         address = request.POST['address']
#         print(name, address)
#         person = Person(name=name, address=address)
#         person.save()
#     return render(request,'index.html')

def index(request):
    displaygotra=GotraData.objects.all()
    displayvidhi=WorkData.objects.all()
    return render(request,'index.html',{'GotraData':displaygotra, 'WorkData':displayvidhi})

def navbar(request):

    return render(request,'modal.html')


def newslip(request):
    if request.method == 'POST':
        client_name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['mobile']
        gotra = request.POST['gotra']
        work_type = request.POST['vidhi']
        amount = request.POST['amount']
        user_name = request.POST['bname']
    
        print(client_name)
        slipData = SlipData(client_name=client_name, address=address, phone=phone, gotra=gotra, work_type=work_type, amount=amount, user_name=user_name )
        slipData.save()
    displaygotra=GotraData.objects.all()
    displayvidhi=WorkData.objects.all()


    return render(request,'newslip.html',{'GotraData':displaygotra, 'WorkData':displayvidhi})


def newbaba(request):
    if request.method == 'POST':
        account_name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        gotra = request.POST['gotra']
        # type = request.POST['btype']
        remarks = request.POST['family']
        print(account_name)
        babaData = Customerdata(account_name=account_name, address=address, phone=phone, gotra=gotra, remarks=remarks )
        babaData.save()
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")
    # displaygotra=GotraData.objects.all()
    # return render(request,'newbaba.html',{'GotraData':displaygotra})

def addvidhi(request):
    if request.method == 'POST':
        work_name = request.POST['vidhi']
        print(work_name)
        vidhiData = WorkData(work_name=work_name)
        vidhiData.save()
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")

def addgotra(request):
    if request.method == 'POST':
        # work_name = request.POST['name']
        gotra_name = request.POST['name']
        print(gotra_name)
        gotraData = GotraData(gotra_name=gotra_name)
        gotraData.save()
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.info(request, f'{username}, you are logged in')
            return redirect('home')
        else:
            # messages.info(request, f'invalid username or password')
            return redirect('login')

    # return render(request,'login.html')
    return HttpResponse("404- Not found")


def logout_user(request):
    logout(request)
    return redirect('home')
    # return HttpResponse('logout')


def userCreate(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=''
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username,email, pass1)
        myuser.save()
        # messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


    # return render(request,'register.html', context)