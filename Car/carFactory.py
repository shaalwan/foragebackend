from car import Car
from datetime import date

from Car.engine.capulet_engine import CapuletEngine
from Car.engine.sternman_engine import SternmanEngine
from Car.engine.willoughby_engine import WilloughbyEngine

from Car.battery.nubbin_battery import NubbinBattery
from Car.battery.spindler_battery import SpindlerBattery

class CarFactory:
    # Callipoe Car
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Capulet Engine & Spindler Battery
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)

        return Car(engine=engine, battery=battery)
    
    # Glissade Car
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        
        # Willoughby Engine & Spindler Battery
        engine = WilloughbyEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        
        return Car(engine=engine, battery=battery)

    # Palindrome Car
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:

        # Sternman Engine & Spindler Battery
        engine = SternmanEngine(warning_light_is_on= warning_light_on)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
        return Car(engine=engine, battery=battery)
    
    # Rorschach Car
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Willoughby Engine & Nubbin Battery
        engine = WilloughbyEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = NubbinBattery(last_service_date= last_service_date, current_date= current_date)

        return Car(engine=engine, battery=battery)

    # Thovex Car
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:

        # Capulet Engine & Nubbin Battery
        engine = CapuletEngine(current_mileage= current_mileage, last_service_mileage= last_service_mileage)
        battery = NubbinBattery(last_service_date= last_service_date, current_date= current_date)
        
        return Car(engine=engine, battery=battery)