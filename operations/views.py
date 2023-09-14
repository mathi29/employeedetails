from django.shortcuts import render, redirect
from operations.forms import EmployeeForm
from operations.models import Employee


def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = EmployeeForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)
  
def update(request, id):
    # Get the employee object by ID
    obj = Employee.objects.get(id=id)

    if request.method == "POST":
        # Pass the instance to the form
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        # Pass the instance to the form
        form = EmployeeForm(instance=obj)

    context = {
        'form': form,
    }
    return render(request, 'update.html', context)


def delete(request, id):
    # Get the employee object by ID
    obj = Employee.objects.get(id=id)

    if request.method == "POST":
        # Delete the employee
        obj.delete()
        return redirect('read')  # Redirect to 'index' view
    
    context = {
        'employee': obj,
    }
    return render(request, 'delete.html', context)


def index(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees': employees})