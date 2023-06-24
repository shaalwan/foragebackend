import unittest

from Car.engine.sternman_engine import SternmanEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        
        engine = SternmanEngine(True)
    
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)

        self.assertFalse(engine.needs_service())