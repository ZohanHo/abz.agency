from django_seed import Seed
from .models import Employee
import random

seeder = Seed.seeder()

# nameList = ["Zohan", "Funky", "blood", "Dick", "Bred", "Bill", "Stive", "Zagara", "Butcher", "Vita"]
# positionList = ['junior developer', 'midle developer', 'sinior developer', 'lead developer', 'pm developer']
# phoneList = "38066"
#
#
# folder_name = '/ '
# folder_name = folder_name.strip()
# img_file_name = "junior", "middle", "lead", "senior", "pm"

#img_name = random.choice(img_file_name)
#file_name = folder_name + img_name + '.jpg'

junior = {
            "name" : "Zoahn",
            'employee_position_q':'junior developer',
            'salary_amount': 1000,
            'foto_employee': "/junior.jpg",
            "parent" : Employee.objects.get(level = 4),
          }

middle = {
            "name" : "Funky",
            'employee_position_q': 'midle developer',
            'salary_amount': 2000,
            'foto_employee': "/middle.jpg",
            "parent" : Employee.objects.get(level = 3),
          }


senior = {
            "name" : "Blood",
            'employee_position_q': 'sinior developer',
            'salary_amount': 3000,
            'foto_employee': "/senior.jpg",
            "parent" : Employee.objects.get(level = 2),
          }

lead = {
            "name" : "Freez",
            'employee_position_q':'lead developer',
            'salary_amount': 4000,
            'foto_employee': "/lead.jpg",
            "parent" : Employee.objects.get(level = 1),
      }

pm = {
            "name" :  lambda x: "Boss",
            'employee_position_q':  lambda x: 'pm developer',
            'salary_amount':  lambda x: 5000,
            'foto_employee':  lambda x: "/pm.jpg",
            "parent" :  lambda x: Employee.objects.get(level = 0),
      }

employee = junior, middle, senior, lead, pm

randm = random.choice(employee)
seeder.add_entity(Employee, 50000, randm)

    # 'name': lambda x:  random.choice(nameList),
    # 'employee_position_q': lambda x:  random.choice(positionList),
    # 'salary_amount': lambda x:  random.randint(1000, 5000),
    # 'foto_employee': lambda x: folder_name + random.choice(img_file_name) + '.jpg',
    # "parent" : lambda x: Employee.objects.get(level = random.randint(1, 4)),
    # #'phone': lambda x:  phoneList + str(random.randint(1000000, 9999999)),

if __name__ == "__main__":
    seeder.execute()