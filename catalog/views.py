from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Employee, Position
from .form import AddEmployeeForm
from django.db.models import Q
import json
#from catalog import seed


def Workerlist(request):
    global employees

    if request.is_ajax():

        #employees = Employee.objects.all()

        #Счтитываем id работника (передавая его через get (onclick="run_show({{ node.id }})"))
        text = request.GET['children_id_to_views']

        # insert id
        node = Employee.objects.get(id=text)

        #get_descendants - создает queryset с потомками в иерархическом порядке, filter + 3 max
        employees = node.get_descendants(include_self = "True").filter(level__lte=node.level + 3)

        data = {}
        data['employees'] = employees
        response = render(request, 'node.html', {'employees': employees})
        return response

    else:
        employees = Employee.objects.all()#.filter(level__lte=1)
        return render(request, "landing_page.html", {'employees': employees})


def WorkerBase(request):
    employees = Employee.objects.all()
    return render(request, 'workerbase.html', context={'employees': employees})

def delemployee(request, pk):
    if request.user.is_authenticated:
        obj = Employee.objects.get(pk__iexact=pk)
        obj.delete()
        return redirect("workerbase")

def create_employee(request):
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
        patent_id = request.POST.get("parent")
        new.parent = Employee.objects.get(id=patent_id)
        new.save()
    return redirect("workerbase")


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    photo = employee.foto_employee
    print(photo)
    form = AddEmployeeForm(request.POST or None,  instance=employee)
    if form.is_valid():
        if request.POST["foto_employee"]:
            employee.foto_employee = request.POST["foto_employee"]
            employee = form.save(commit=False)
            employee.save()
        else:
            employee = form.save(commit=False)
            employee.save()
        return redirect("workerbase")
        #return HttpResponseRedirect(instance.get_absolute_url_update())     # редирект на деталку
    return render(request, "update.html", context={"form":form, "instanse": employee})


# def search_ajax(request):
#     data = {}
#     result_list = []
#     value_input = request.GET.get('value_input', None)
#     print(request.GET)
#
#     if value_input:
#         result_list = [
#             (user.employee_position_q,
#              user.name,
#              str(user.salary_amount),
#              str(user.date),
#              ) for user in Employee.objects.filter(
#             Q(employee_position_q__icontains=value_input) |
#             Q(name__icontains=value_input)|
#             Q(salary_amount__icontains=value_input) |
#             Q(date__icontains=value_input)
#             )
#         ]
#         data = {
#             "result": result_list,
#             "value_input": value_input,
#         }
#     # возвращает строку, представляющую объект json из объекта
#     return HttpResponse(json.dumps(data))

def sort_ajax(request):
    if request.user.is_authenticated and request.user != "AnonymousUser":
        if request.is_ajax():
            sort_by = request.GET['sort_by']
            search_text = request.GET['q_search']

            employees = Employee.objects.order_by(sort_by).filter(Q(employee_position_q__icontains=search_text))
            employees = employees | Employee.objects.order_by(sort_by).filter(Q(name__icontains=search_text))
            employees = employees | Employee.objects.order_by(sort_by).filter(Q(salary_amount__icontains=search_text))
            employees = employees | Employee.objects.order_by(sort_by).filter(Q(date__icontains=search_text))

            context = {}

            # current_page = Paginator(list(employees), 20)
            # page = request.GET['page']
            # try:
            #     context['employees'] = current_page.page(page)
            # except PageNotAnInteger:
            #     context['employees'] = current_page.page(1)
            # except EmptyPage:
            #     context['employees'] = current_page.page(current_page.num_pages)
            #print(context)

            context['employees'] = employees

            response = render(request, 'employees_all_sort.html', context)
            return response
        else:
            employees = Employee.objects.order_by('date')
            context = {}

            # current_page = Paginator(list(employees), 20)
            # page = request.GET.get('page')
            # try:
            #     context['employees'] = current_page.page(page)
            # except PageNotAnInteger:
            #     context['employees'] = current_page.page(1)
            # except EmptyPage:
            #     context['employees'] = current_page.page(current_page.num_pages)

            context['employees'] = employees
            return render(request, 'workerbase.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/')

def task(request):
    return render(request, "task.html")