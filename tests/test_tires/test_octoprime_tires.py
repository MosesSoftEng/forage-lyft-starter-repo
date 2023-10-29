import unittest
from typing import List

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self) -> None:
        """
        Test tires should be serviced when sum of tire wears is equal or greater than 3.

        :param self: The test case instance.
        :return: None
        """
        tires_wear: List[float] = [1.0, 0.0, 1.0, 1.0]

        tires: OctoprimeTires = OctoprimeTires(tires_wear)

        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self) -> None:
        """
        Test tires should be not be serviced when sum of tire wears is less than 3.

        :param self: The test case instance.
        :return: None
        """
        tires_wear: List[float] = [0.0, 1.0, 1.0, 0.9]

        tires: OctoprimeTires = OctoprimeTires(tires_wear)

        self.assertFalse(tires.needs_service())
