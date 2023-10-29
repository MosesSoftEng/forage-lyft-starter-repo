import unittest
from datetime import date

from batteries.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self) -> None:
        """
        Test battery should be serviced when difference between current date and last service date is above service
                limit threshold.

        :param self: The test case instance.
        :return: None
        """
        current_date: date = date.fromisoformat("2003-01-01")
        last_service_date: date = date.fromisoformat("2000-01-01")
        battery: SpindlerBattery = SpindlerBattery(
            current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self) -> None:
        """
        Test battery should not be serviced when difference between current date and last service date is below service
                limit threshold.

        :param self: The test case instance.
        :return: None
        """
        current_date: date = date.fromisoformat("2001-12-31")
        last_service_date: date = date.fromisoformat("2000-01-01")
        battery: SpindlerBattery = SpindlerBattery(
            current_date, last_service_date)

        self.assertFalse(battery.needs_service())
