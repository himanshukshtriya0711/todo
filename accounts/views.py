from django.shortcuts import render


def login(request):
    return render(request,"accounts/login.html")


#=======================register================

def register(request):
    return render(request,"accounts/register.html")
