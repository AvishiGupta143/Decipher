from django.shortcuts import render, redirect
import smtplib
import ssl
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
import random
import json
import boto3
import time
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static


def Homepage(request):
    Data = {}
    if request.user.id is not None:
        Data = {
            'Profile': Profile.objects.get(user=request.user)
        }
    return render(request, "Homepage.html", Data)


def Assignment(request):
    return render(request, "AssignmentPage.html")


def ProfilePage(request):
    Data = {}
    if request.user.id is not None:
        Data = {
            'Profile': Profile.objects.get(user=request.user)
        }
        return render(request, "Profile.html", Data)
    return redirect('/Decipher')


def EmailVerification(request):
    Data = {
        'Email': Profile.objects.get(user=request.user).Email,
    }
    return render(request, "EmailVerification.html", Data)


def SendCodeEmail(request):
    print(request.POST)
    Code = random.randint(150000, 999999)
    sender = "authorspointhelp@gmail.com"
    password = "authorspoint123@"
    port = 465
    recieve1 = request.POST['To_Email']
    cont = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=cont) as server:
        server.login(sender, password)
        subject = 'Verification Code'
        body = f"""Verification Code for your account
                   Code:  {Code}"""
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender, recieve1, message)
    ctx = {'result': 'Done', 'Code': str(Code)}
    return HttpResponse(json.dumps(ctx), content_type='application/json')


def SendCodePhone(request):
    print(request.POST)
    New = random.randint(150000, 999999)
    Message = f'Verification Code for Assignment Project is = {New}'
    client = boto3.client('sns', 'ap-south-1')
    client.publish(PhoneNumber=f'{request.POST["To_Phone"]}', Message=Message)
    ctx = {'result': 'Done', 'Code': f'{New}'}
    return HttpResponse(json.dumps(ctx), content_type='application/json')


def ApplyVerifyEmail(request):
    New = Profile.objects.get(Email= request.POST['Email'])
    New.Email_Verified = 'Verified'
    New.save()
    return redirect('/Decipher')


def ApplyVerifyPhone(request):
    New = Profile.objects.get(Contact=request.POST['Contact'])
    New.Phone_Verified = 'Verified'
    New.save()
    return redirect('/Decipher')


def PhoneVerification(request):
    Data = {
        'Contact': Profile.objects.get(user=request.user).Contact,
    }
    return render(request, "PhoneVerification.html", Data)


def Register(request):
    if request.user.id is not None:
        return redirect('/Decipher')
    if request.method == 'POST':
        New = User()
        New.username = request.POST['Username']
        New.email = request.POST['Email']
        New.set_password(request.POST['Password1'])
        New.save()

        NewProfile = Profile()
        NewProfile.user = New
        NewProfile.Email = request.POST['Email']
        NewProfile.Contact = request.POST['Phone']
        NewProfile.Verified = 'False'
        NewProfile.Unique_ID = 'Select_Dine_' + str(random.randint(150000, 99999999)) + '_' + New.username + '_SD'
        NewProfile.save()
        return redirect('/Decipher/Login')
    else:
        return render(request, "Register.html")


def Login(request):
    if request.user.id is not None:
        return redirect('/Decipher')
    else:
        if request.method == 'POST':
            username = request.POST['Username']
            password = request.POST['Password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/Decipher')
        else:
            user = request.user
            if user.id is None:
                return render(request, "Login.html")
            else:
                return redirect('/Decipher')


def Logout(request):
    if request.user.id is None:
        return redirect('/Decipher')
    else:
        auth.logout(request)
        return redirect('/Decipher')


def CheckUsernameUniqueness(request):
    if request.method == 'POST':
        message = ""
        if User.objects.filter(username=request.POST['Username']).exists():
            message = 'Exists'
        else:
            message = 'Not Exists'
        ctx = {'result': message}
        return HttpResponse(json.dumps(ctx), content_type='application/json')


def CheckPasswordCorrectness(request):
    if request.method == 'POST':
        message = ""
        if User.objects.filter(username=request.POST['Username']).exists():
            if check_password(request.POST['Password'], User.objects.get(username=request.POST['Username']).password):
                message = 'Correct'
            else:
                message = 'Incorrect'
        else:
            message = 'Incorrect'
        ctx = {'result': message}
        return HttpResponse(json.dumps(ctx), content_type='application/json')


def CheckEmailUniqueness(request):
    if request.method == 'POST':
        message = ""
        if ('@' not in request.POST['Email']) or ('.com' not in request.POST['Email']):
            message = 'Invalid Email'
        elif User.objects.filter(email=request.POST['Email']).exists():
            message = 'Exists'
        else:
            message = 'Not Exists'
        ctx = {'result': message}
        return HttpResponse(json.dumps(ctx), content_type='application/json')
