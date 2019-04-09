"""abz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', task, name="task_url"),
    path('worker/', Workerlist, name="workerlist"),
    path('base/', WorkerBase, name="workerbase"),
    path('base/<pk>/del', delemployee, name="del_employee"),
    path('base/<pk>/edit', update_employee, name="update_employee_url"),
    path('base/create/', create_employee, name="create_employee_url"),
    path('base/create/save', save_employee, name="save_employee_url"),
    path('sort_ajax/', sort_ajax, name="sort_ajax_url"),
]
