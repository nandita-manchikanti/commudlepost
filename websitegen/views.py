from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib import messages
from .forms import MemberForm

def Home(request):
        form=MemberForm()
        error=""
        if request.method == "POST":
           MemberForm(request.POST,request.FILES).save()
        context={'form':form,'error':error}
        return render(request,'home.html',context)

def Portfolio(request):
    error=""
    member=Member.objects.first()
    d={'member':member,'error':error}
    return render(request,"portfolio.html",d)