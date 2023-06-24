import unittest

from Car.engine.willoughby_engine import WilloughbyEngine

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 90001
        last_service_mileage = 30000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 80000
        last_service_mileage = 70000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)

        self.assertFalse(engine.needs_service())