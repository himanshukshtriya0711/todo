from django.shortcuts import render,redirect
from django.contrib.auth.models import User #register krte time pe import
from django.contrib import auth   #ismein method hote hai 3 (authenticate ,login,register) login krte time pr import
#======================================login======================
def login(request):
    if request.method=="POST":
        #template wala data view mein lekr aa re hai
        input_username = request.POST.get("name")
        input_password = request.POST.get("password")

        user = auth.authenticate(username =input_username,password = input_password)

        if user is not None:
            auth.login(request,user) #session create ho gya hai or request ke pass user ki saari detail hai #yeh user upar wla hi hai line 11 wla
            return redirect("todo")                         # yeh request bhi ypar wala hi hai function wla line 5
           
        else:
            return redirect("home")

        


    return render(request,"accounts/login.html")


#=======================register================

def register(request):
    if request.method == "POST":
        #template wala data view mein lekr aa re hai
        input_username = request.POST.get("username")  #register.html wala name hai yeh html wla
        input_password = request.POST.get("password")

         # view wala data model mein save re hai
        new_user = User(
            username = input_username
            # password = input_password


        )
        new_user.set_password(input_password) # pasword ko save krne ka tareeka alg hota hai
        new_user.save()
        return redirect("login")


    return render(request,"accounts/register.html")

#=================log put (button or url khud set krni hai bhaiya ne nhi karai)=========
def logout(request):
    auth.logout(request)
    return redirect("login")