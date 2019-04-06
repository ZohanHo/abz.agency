from django_seed import Seed
from .models import Employee
import random

seeder = Seed.seeder()

nameList = ["Zohan", "Funky", "blood", "Dick", "Bred", "Bill", "Stive", "Zagara", "Butcher", "Vita"]
positionList = ['junior developer', 'midle developer', 'sinior developer', 'lead developer', 'pm developer']
phoneList = "38066"

seeder.add_entity(Employee, 10, {
    'name': lambda x:  random.choice(nameList),
    'employee_position_q': lambda x:  random.choice(positionList),
    'salary_amount': lambda x:  random.randint(1000, 5000),
    #"parent" : lambda x:  random.choice(Employee.parent.choices(positionList)),
    #'phone': lambda x:  phoneList + str(random.randint(1000000, 9999999)),

})

#if __name__ == "__main__":
inserted_pks = seeder.execute()



