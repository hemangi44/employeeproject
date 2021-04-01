from django.shortcuts import render,redirect
from .models import DepartmentModel
from .forms import DepartmentForm
from .models import EmployeeModel
from .forms import EmployeeForm

# Create your views here.


# Create your views here.
def home(request):
    return render(request, 'home.html')

def showdept(request):
    data = DepartmentModel.objects.all()
    return render(request, 'showdept.html', {'data':data})

def adddept(request):
    if request.method == "POST":
        f = DepartmentForm(request.POST)
        if f.is_valid():
            f.save()
            fm = DepartmentForm()
            return render(request, 'adddept.html', {'fm':fm,'msg':'Dept Added'})
        else:
            return render(request, 'adddept.html', {'fm':f,'msg':'Check Errors'})
    else:
        fm = DepartmentForm()
        return render(request, 'adddept.html', {'fm':fm})

def deletedept(request, id):
    d = DepartmentModel.objects.get(deptid=id)
    d.delete()
    return redirect('showdept')

def showinfo(request):
    data = EmployeeModel.objects.all()
    return render(request, 'showinfo.html', {'data':data})

def addinfo(request):
    if request.method == "POST":
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            fm = EmployeeForm()
            return render(request, 'addinfo.html', {'fm':fm,'msg':'Employee Added'})
        else:
            return render(request, 'addinfo.html', {'fm':f,'msg':'Check Errors'})
    else:
        fm = EmployeeForm()
        return render(request, 'addinfo.html', {'fm':fm})

def deleteinfo(request, id):
    d = EmployeeModel.objects.get(empid=id)
    d.delete()
    return redirect('showinfo')

def search(request):
    ns = request.GET.get('Search')
    data = EmployeeModel.objects.filter(address=ns)
    return render(request, 'showinfo.html', {'data':data})
