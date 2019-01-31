from Worker import Worker

import datetime


class Employee(Worker):

    def __init__(self, salary_p_year: float, id_worker: int, first_name: str, last_name: str, hire_date: datetime):
        self.__salary_p_year = float(salary_p_year)
        super().__init__(id_worker, first_name, last_name, hire_date)

    def get_cost_p_hour(self):
        working_days = 261
        hours_p_day = 8
        __cost_p_hour = self.__salary/(working_days*hours_p_day)
        return __cost_p_hour

    def set_salary(self, salary_p_year):
        self.__salary_p_year = float(salary_p_year)



