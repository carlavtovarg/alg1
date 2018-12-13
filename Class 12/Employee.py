class Worker:
    """"This is the inicialization of worker class"""
    def __init__(self, worker_name=""):
        self.__name = worker_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

class Employee(Worker):
    """"This class specializes worker and is salaried"""
    def __init__(self, initial_salary, initial_name):
        self.__salary = initial_salary
        super().__init__(initial_name)

    def set_employee(self, new_salary):
        self.__salary = new_salary

    def get_employee(self):
        return self.__salary

new_employee = Employee(2000,"Luisa")
print(new_employee.get_employee())