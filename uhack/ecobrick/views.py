from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect,redirect,HttpResponse, reverse, get_object_or_404, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views import generic
from .models import *
from .forms import *
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout

import datetime
# import timezone
#LOGIN
def login_view(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    title = "Login"
    form = login(request.POST or None)
    context = {"form":form, "title": title,"loggeduser":loggeduser}
    all_users = UserDetail.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for user in all_users:
            if user.username == username:
                if user.password == password:
                    request.session['user'] = user.id
                    if user.userType == 0:
                        return redirect('staff')
                    else:
                        return redirect("home")
            else:
                context['log_error'] = "Cannot find an account with that combination"

    return render(request, "login.html", context)


def homepage(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    return render(request,"home.html",{'loggeduser':loggeduser})

def rewards(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0
    rewards = Reward.objects.all()
    myRewards = MyReward.objects.filter(user=loggeduser)
    if request.method == "POST":
        for i in request.POST:
            if i[:4] == "del-":
                toDel = i[4:]
                reward = Reward.objects.get(id=toDel)
                temp = loggeduser.brickPoints - reward.pointCost
                if temp >= 0:
                    loggeduser.brickPoints -= reward.pointCost
                    loggeduser.save()
                    new_reward = MyReward(user=loggeduser, rewardName=reward.rewardName, pointCost=reward.pointCost, description=reward.description)
                    new_reward.save()
    return render(request, "rewards.html", {"rewards": rewards, "myRewards": myRewards,'loggeduser':loggeduser})

def partners(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0
    return render(request, "partners.html", {'loggeduser':loggeduser})
#REGISTER
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         form2 = UserDetailsForm(request.POST)
#         if form.is_valid() and form2.is_valid():
#             user = form.save(commit=False)
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#
#             try:
#                 validate_password(password,email)
#             except ValidationError as e:
#                 form.add_error('password',e)
#                 return render(request, 'leverageapp/register_bs4.html',{'form':form,'form2':form2})
#
#             user.set_password(password)
#             user.save()
#             #user.groups.add(Group.objects.get(name='Client'))
#
#
#             user_details = form2.save(commit=False)
#             user_details.user = user
#             user_details.save()
#
#             return HttpResponse('WELCOME TO LEVERAGE')
#     else:
#         form = UserForm()
#         form2 = UserDetailsForm()
#     return render(request, 'leverageapp/register_bs4.html', {'form': form, 'form2':form2})

#LOGOUT
def logout_view(request):
    #logout(request)
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    del request.session['user']

    return HttpResponseRedirect('/')

def staff_view(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    all_users = UserDetail.objects.all()
    title = "Staff page"
    success = ""

    if request.method == "POST":
        if "userId" in request.POST:
            if "numEcobrick" in request.POST:
                username = request.POST.get("userId")
                num = request.POST.get("numEcobrick")
                weight = request.POST.get("weightEco")

                user = get_object_or_404(UserDetail,username=username)

                user.brickNum = user.brickNum + int(num)
                user.brickWeight = user.brickWeight + int(weight)
                user.brickPoints = user.brickWeight + int(weight)
                user.save()

                return render(request,'admin.html',{'title':title,'success':"Eco brick successfully added",'loggeduser':loggeduser})

    return render(request,'admin.html',{'title':title,'success':success,'loggeduser':loggeduser})

def user_profile(request, userid):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    user = UserDetail.objects.get(id=userid)

    context = {
        'loggeduser': loggeduser,
        'user':user,
    }

    return render(request,'userprofile.html',context)

def register_view(request):
    form = register(request.POST or None)

    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    context = {"form":form, 'loggeduser':loggeduser}

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'register.html', context)

def about(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    return render(request,'about.html',{'loggeduser':loggeduser})

def leaderboard(request):
    top_users =  UserDetail.objects.all().order_by('-brickWeight')[:10]
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0


    context = {
        'top_users':top_users,
        'loggeduser':loggeduser,
    }

    return render(request, 'leaderboard.html', context)

def subscription(request):
    try:
        loggeduser = UserDetail.objects.get(id=request.session['user'])
    except(KeyError, UserDetail.DoesNotExist):
        loggeduser = 0

    context = {
        'loggeduser': loggeduser,
    }

    return render(request,'subscription.html',context)
