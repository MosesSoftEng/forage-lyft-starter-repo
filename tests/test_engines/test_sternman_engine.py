import unittest

from engines.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self) -> None:
        """
        Test engine should be serviced when warning light is on

        Parameters:
                self (TestClassName): The instance of the test class.

        Returns:
                None
        """
        warning_light_is_on: bool = True
        engine: SternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self) -> None:
        """
        Test engine should not be serviced when warning light is off.

        Parameters:
                self (TestClassName): The instance of the test class.

        Returns:
                None
        """
        warning_light_is_on: bool = False
        engine: SternmanEngine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
