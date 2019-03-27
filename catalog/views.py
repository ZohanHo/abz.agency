from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Employee, Position
from .form import AddEmployeeForm
from django.db.models import Q
import json

# Create your views here.
def Workerlist(request):
    employee = Employee.objects.all()


    return render(request, 'landing_page.html', context={'employee': employee})

def WorkerBase(request):
    employee = Employee.objects.all()
    return render(request, 'workerbase.html', context={'employee': employee})

def delemployee(request, pk):
    if request.user.is_authenticated:
        obj = Employee.objects.get(pk__iexact=pk)
        obj.delete()
        return redirect("workerbase")


def create_employee(request):
    #Employee.objects.get_or_create()


    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=Employee)
        if form.is_valid():
            form.save()
    else:
        form = AddEmployeeForm()

    return render(request, "create.html", context={"form":form})

def save_employee(request):

    if request.method == 'POST':

        new = Employee()
        new.name = request.POST.get("name")
        new.salary_amount = request.POST.get("salary_amount")
        new.foto_employee = request.POST.get("foto_employee")
        new.employee_position_q = request.POST.get("employee_position_q")
        #new.parent = request.POST.get("parent")

        new.save()

    return redirect("workerbase")

def update_employee(request, pk):
    instance = Employee.objects.get(pk=pk)

    form = AddEmployeeForm(request.POST or None,  instance=instance)


    if form.is_valid():
        instance.foto_employee = request.POST.get("foto_employee")
        instance = form.save(commit=False)
        instance.save()


        return redirect("workerbase")
        #return HttpResponseRedirect(instance.get_absolute_url_update())     # редирект на деталку
    return render(request, "update.html", context={"form":form, "instanse":instance})

def sort(request):

    #Sort
    employees = Employee.objects.all()
    if request.GET.get('name'):
        employees = Employee.objects.order_by("name")
    if request.GET.get('salary'):
        employees = Employee.objects.order_by("-salary_amount")
    if request.GET.get('position'):
        employees = Employee.objects.order_by("employee_position_q")
    if request.GET.get('date'):
        employees = Employee.objects.order_by("-date")

    return render(request, 'workerbase.html', context={'employee': employees})


def search(request):
    # Search
    search_text = request.GET['search']
    employees = Employee.objects.filter(Q(employee_position_q__icontains=search_text))
    employees = employees | Employee.objects.filter(Q(name__icontains=search_text))
    employees = employees | Employee.objects.filter(Q(salary_amount__icontains=search_text))
    employees = employees | Employee.objects.filter(Q(date__icontains=search_text))

    return render(request, 'workerbase.html', context={'employee': employees})