import datetime


class Worker:

    def __init__(self, id_worker:int, first_name: str, last_name: str, hire_date: datetime):
        self.__id = id_worker
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return  self.__last_name

    def get_hire_date(self):
        return self.__hire_date


class Employee(Worker):

    def __init__(self, salary_p_year: float, id_worker: int, first_name: str, last_name: str, hire_date: datetime):
        self.__salary_p_year = float(salary_p_year)
        super().__init__(id_worker, first_name, last_name, hire_date)

    def get_cost_p_hour(self):
        working_days = 261
        hours_p_day = 8
        cost_p_hour = self.__salary_p_year/(working_days*hours_p_day)
        return cost_p_hour

    def set_salary(self, salary_p_year):
        self.__salary_p_year = float(salary_p_year)

    def get_salary(self):
        return self.__salary_p_year


class Contractor(Worker):

    def __init__(self, cost_p_hour, id_worker: int, first_name: str, last_name: str, hire_date: datetime):
        super().__init__(id_worker, first_name, last_name, hire_date)
        self.__cost_p_hour = float(cost_p_hour)

    def get_cost_p_hour(self):
        return self.__cost_p_hour

    def set_cost_p_hour(self, cost_p_hour):
        self.__cost_p_hour = float(cost_p_hour)


class Task:
    def __init__(self, task_id: int, name: str, description: str, assigned_to: Worker, duration: float):
        """when we make assigned_to: Worker, thats include Employee and Contractor automacticly"""
        self.__task_id = task_id
        self.__name = name
        self.__description = description
        self.__assigned_to = assigned_to
        self.__duration = duration
        self.__hours_completed = 0.0

    def set_name(self, name: str):
        self.__name = name

    def set_description(self, description: str):
        self.__description = description

    def set_duration(self, duration: float):
        self.__duration = duration

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__task_id

    def get_desc(self):
        return self.__description

    def set_assigned_to(self, assigned_to: Worker):
        self.__assigned_to = assigned_to

    def get_duration(self):
        return self.__duration

    def get_assigned_to(self):
        return self.__assigned_to

    def get_hours_completed(self):
        return self.__hours_completed

    def add_time(self, num_hours: float):
        self.__hours_completed += num_hours


class Project:
    def __init__(self, id_proj: int, name, hour_est: float):
        self.id = id_proj
        self.__name = name
        self.__hour_est = hour_est
        self.__tasks = []

    def set_task(self, task_id: Task):
        self.__tasks.append(task_id)

    def set_name(self, name):
        self.__name = name

    def set_hours_est(self, hour_est):
        self.__hour_est = hour_est

    def get_name(self):
        return self.__name

    def get_hour_est(self):
        return self.__hour_est

    def get_task(self):
        return self.__tasks

    def get_project_cost(self):
        total_cost = 0
        for t in self.__tasks:
            total_cost += (t.get_duration()) * (t.get_assigned_to().get_cost_p_hour())
        print("Total Cost:" + str(total_cost))

    def get_hours_completed(self):
        total_hours = 0.00
        for t in self.__tasks:
            total_hours += (t.get_hours_completed())
        print("Total Hours Completed:" + str(total_hours))


emp1 = Employee(75000, 1, "Carla", "Tovar", "2018/12/12")

print(emp1.get_cost_p_hour())


task1 = Task(1, "definition", "create bla babla", emp1, 50)
print(task1.get_assigned_to().get_id())

task2 = Task(2, "concept", "create bla ", emp1, 50)
print(task2.get_assigned_to().get_id())

project = Project(1, "House", 200)
project.set_task(task1)
print(task1.get_id())

project.set_task(task2)
print(task2.get_id())
project.get_project_cost()
task1.add_time(10)
task2.add_time(10)
project.get_hours_completed()

