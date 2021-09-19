from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    """In this function data will add and Show"""
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # form.save()            # ----- we can save directly after valid
            nm = form.cleaned_data["name"]       # ---- another method getting field first before saving to database
            em = form.cleaned_data["email"]
            pw = form.cleaned_data["password"]
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            form = StudentRegistration()     # --- to show blank form after saving 

    else:
        form = StudentRegistration() 
    std = User.objects.all()
    return render(request, "add_show.html", {"form":form, "stu":std})


def delete_data(request, id):
    """In this function is to delete data"""
    if request.method == "POST":
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect("/")


def update_data(request, id):
    """In this function udate data"""
    if request.method == "POST":
        d = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=d)
        if form.is_valid():
            form.save()
    else:
        d = User.objects.get(pk=id)
        form = StudentRegistration(instance=d)

    return render(request, "update.html", {"form": form})