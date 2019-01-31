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
    def __init__(self, id, name, hour_est):
        self.id = id
        self.name = name
        self.hour_est = hour_est
        self.task = []

    def set_task(self, task_id: Task):
        self.task.append(task_id)

    def set_name(self, name):
        self.name = name

    def set_hours_est(self, hour_est):
        self.hour_est = hour_est

    def get_name(self):
        return self.name

    def get_hour_est(self):
        return self.hour_est

    def get_task(self):
        return self.task


emp1 = Employee(75000, 1, "Carla", "Tovar", "2018/12/12")

print(emp1.get_cost_p_hour())


task1 = Task(1, "definicion", "create bla babla", emp1, 18)
print(task1.get_assigned_to().get_id())