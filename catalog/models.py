from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey



class Position(models.Model):
    job_title = models.CharField(max_length=120, default="junior")

    def __str__(self):
        return "{}".format(self.job_title)

    class Meta:
        verbose_name = "Должность сотрудника"
        verbose_name_plural = "Должности сотрудников"


CHOICES = (
    ('junior developer', 'junior developer'),
    ('midle developer', 'midle developer'),
    ('sinior developer', 'sinior developer'),
    ('lead developer', 'lead developer'),
    ('pm developer', 'pm developer'),
)

class Employee(MPTTModel):
    name = models.CharField(max_length=100)
    employee_position_q= models.CharField(max_length=30, choices=CHOICES)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    salary_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    foto_employee = models.ImageField(blank = False, upload_to="images/%Y/%m/%d", verbose_name = 'employment_photo', help_text = '150x150px' )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    def __str__(self):
        return "ФИО: {}".format(self.name)

    class Meta:
        verbose_name = "Информация о сотруднике"
        verbose_name_plural = "Информация о сотрудниках"

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url_del(self):
        return reverse("del_employee", kwargs={"pk": self.pk})

    def get_absolute_url_update(self):
        return reverse("update_employee_url", kwargs={"pk": self.pk})
