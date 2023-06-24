from .battery import Battery
from datetime import date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        # super().__init__(last_service_date)
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):

        # 2 Years
        return (self.__current_date - self.__last_service_date).days > (365 * 3)