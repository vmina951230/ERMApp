from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def emp_form(request,id=0):
    if(request.method == "GET"):
        if(id==0):
            form = EmployeeForm()
        else:
            p = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=p)
        return render(request, 'emp_form.html', {'form': form})
    else:
        if(id==0):
            form = EmployeeForm(request.POST)
        else:
            p = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=p)
        if(form.is_valid()):
            form.save()
        return redirect('/employee/list')

def emp_list(request):
    context = {"employee_list":Employee.objects.all()}
    return render(request, 'emp_list.html', context)
def emp_delete(request,id):
    p = Employee.objects.get(pk=id)
    p.delete()
    return redirect('/employee/list')