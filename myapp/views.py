from django.shortcuts import render,redirect
from .models import Todo , Profile
#========================HOME======================
def home(request):
    
    return render(request,"home.html")


#========================Todo======================

def todo(request):
    todos = Todo.objects.filter(is_completed=False)
    parameter={
        "todos":todos,
        
    }
    return render(request,"todo.html",parameter)

#========================ADD_todo=================

def add_todo(request):
    if request.method=="POST":
        user_task = request.POST.get("text")
        user_created_at = request.POST.get("created_at")
        
        
        new_todo = Todo(
            text = user_task, created_at = user_created_at #Object create kara hai naya
            )
        new_todo.save()
        return redirect ("todo") 
        
    return render(request,"add_todo.html")

#=========================DELETE TASK=============

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect("todo")

#=========================UPDATE TASK=============

def update_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method=="POST":
        user_task = request.POST.get("text")
        user_created_at = request.POST.get("created_at")  
        
        
        todo.text = user_task
        todo.created_at = user_created_at
        todo.save()
    
        return redirect("todo")
        
    
    parameters = {
        'todo' : todo
    }
    return render(request,"update_todo.html",parameters)
   
#======================mark_complete===============

def mark_complete(request,todo_id):
    todo = Todo.objects.get(id = todo_id)

    todo.is_completed = True
    todo.save()

    return redirect("todo")

#=====================Uploading_pic=================

def upload_profile(request):
    if request.method=="POST":
        profile_pic = request.FILES["profile_pic"] #files ko ya image ko get krne ka tareeka
        new_profile = Profile(
            title = "demo title",    #nya object create kia hai
            profile_pic = profile_pic

        )
        new_profile.save()
        return redirect("home")
    return render(request,"upload_profile.html")



