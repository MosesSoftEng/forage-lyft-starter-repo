import datetime
import unittest

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
	def test_engine_should_be_serviced(self) -> None:
		"""
		Test case to verify if the engine should be serviced based if current mileage exceeds service limit threshold.

		Parameters:
		- self: The test case instance.

		Returns:
		- None
		"""
		current_mileage:int = 30001
		last_service_mileage:int = 0

		engine: CapuletEngine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.needs_service())

	def test_engine_should_not_be_serviced(self) -> None:
		"""
		Test case to verify that the engine should not be serviced when the current mileage is below than service
			limit threshold.

		:param self: The test case instance.
		:return: None
		"""
		current_mileage:int = 30000
		last_service_mileage:int = 0

		engine: CapuletEngine = CapuletEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.needs_service())


if __name__ == "main":
	unittest.main()
