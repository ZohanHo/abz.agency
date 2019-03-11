from django.shortcuts import render
from .models import Employee

# Create your views here.
def Workerlist(request):
    employee = Employee.objects.all()
    return render(request, 'landing_page.html', context={'employee': employee})

def WorkerBase(request):
    employee = Employee.objects.all()
    return render(request, 'workerbase.html', context={'employee': employee})