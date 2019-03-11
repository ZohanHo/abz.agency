from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Position(models.Model):
    job_title = models.CharField(max_length=120)

    def __str__(self):
        return "{}".format(self.job_title)

    class Meta:
        verbose_name = "Должность сотрудника"
        verbose_name_plural = "Должности сотрудников"


class Employee(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    employee_position = models.ForeignKey('Position', null=True, blank=True, on_delete=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    salary_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    foto_employee = models.ImageField(upload_to="static/images/", default="")

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    def __str__(self):
        return "ФИО: {}".format(self.name)

    class Meta:
        verbose_name = "Информация о сотруднике"
        verbose_name_plural = "Информация о сотрудниках"

    class MPTTMeta:
        order_insertion_by = ['name']

    # def get_absolute_url(self):
    #     return reverse("********", kwargs={"pk": self.pk})



# class Genre(MPTTModel):
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#
#     class MPTTMeta:
#         order_insertion_by = ['name']