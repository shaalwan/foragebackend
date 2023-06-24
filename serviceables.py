from abc import ABC, abstractmethod
class Serviceable(ABC):

    @abstractmethod
    def needs_service() -> bool:
        pass