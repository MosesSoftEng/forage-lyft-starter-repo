import unittest
from datetime import date

from batteries.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self) -> None:
        """
        Test battery should be serviced when difference between current date and last service date is above service
                limit threshold.

        :param self: The test case instance.
        :return: None
        """
        current_date: date = date.fromisoformat("2004-01-01")
        last_service_date: date = date.fromisoformat("2000-01-01")
        battery: NubbinBattery = NubbinBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self) -> None:
        """
        Test battery should not be serviced when difference between current date and last service date is below service
                limit threshold.

        :param self: The test case instance.
        :return: None
        """
        current_date: date = date.fromisoformat("2003-12-31")
        last_service_date: date = date.fromisoformat("2000-01-01")
        battery: NubbinBattery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())
