import unittest
from typing import List

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self) -> None:
        """
        Test tires should be serviced when one of tire wears is equal or greater than 0.9.

        :param self: The test case instance.
        :return: None
        """
        tires_wear: List[float] = [0.0, 0.1, 0.9, 0.5]

        tires: CarriganTires = CarriganTires(tires_wear)

        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self) -> None:
        """
        Test tires should not be serviced when none of tire wears is equal or greater than 0.9.  

        :param self: The test case instance.
        :return: None
        """
        tires_wear: List[float] = [0.0, 0.1, 0.8, 0.5]

        tires: CarriganTires = CarriganTires(tires_wear)

        self.assertFalse(tires.needs_service())
