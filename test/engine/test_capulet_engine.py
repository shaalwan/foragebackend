import unittest

from Car.engine.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 30000
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 3000
        last_service_mileage = 8000
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertFalse(engine.needs_service())