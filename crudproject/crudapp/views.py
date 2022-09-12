import re
from textwrap import indent
from django.shortcuts import render,redirect

from crudapp.forms import StudentForm
from crudapp.models import Student

# Create your views here.

def home(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
    form=StudentForm()
    obj=Student.objects.all()
    templates_name='index.html'
    context={'form':form,'obj':obj}
    return render(request,templates_name,context)

def delete(request,id):
    obj=Student.objects.get(id=id)
    obj.delete()
    return redirect('home')


def update(request,id):
    obj=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect("home")
    form=StudentForm(instance=obj)
    templates_name='update.html'
    context={'form':form}
    return render(request,templates_name,context)