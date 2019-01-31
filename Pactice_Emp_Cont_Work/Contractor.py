from Worker import Worker
import datetime


class Contractor(Worker):

    def __init__(self, cost_p_hour, id_worker: int, first_name: str, last_name: str, hire_date: datetime):
        super().__init__(id_worker, first_name, last_name, hire_date)
        self.__cost_p_hour = float(cost_p_hour)

    def get_cost_p_hour(self):
        return self.__cost_p_hour

    def set_cost_p_hour(self, cost_p_hour):
        self.__cost_p_hour = float(cost_p_hour)
