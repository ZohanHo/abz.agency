from django.contrib import admin
from .models import Employee, Position

class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields]

    class Meta:
        model = Position

admin.site.register(Position, PositionAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

    class Meta:
        model = Employee

admin.site.register(Employee, EmployeeAdmin)



