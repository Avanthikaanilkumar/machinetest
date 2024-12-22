from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def employee(request):
    a=Employee.objects.all()
    return render(request,'',{'employee1':a})
def add_emp(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('a')
        else:
            form=EmployeeForm()
            return redirect(request,'add_emp.html',{'form':form})



