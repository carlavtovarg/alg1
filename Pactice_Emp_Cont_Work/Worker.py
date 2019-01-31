import datetime
class Worker:

    def __init__(self, id_worker:int, first_name: str, last_name: str, hire_date: datetime):
        self.__id = id_worker
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def get_id(self):
        return self.__id



