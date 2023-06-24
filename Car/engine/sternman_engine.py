from .engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        # super().__init__(last_service_date)
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.__warning_light_is_on