import unittest

from engines.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self) -> None:
        """
        Test engine should be serviced when current mileage exceeds service limit threshold.

        Parameters:
            self: The current instance of the test class.

        Returns:
            None
        """
        current_mileage: int = 60001
        last_service_mileage: int = 0
        engine: WilloughbyEngine = WilloughbyEngine(
            current_mileage, last_service_mileage
        )

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self) -> None:
        """
        Test engine should not be serviced when current mileage is below service limit threshold.

        Parameters:
        - self: The instance of the test case class.

        Returns:
        - None
        """
        current_mileage: int = 60000
        last_service_mileage: int = 0
        engine: WilloughbyEngine = WilloughbyEngine(
            current_mileage, last_service_mileage
        )

        self.assertFalse(engine.needs_service())
