from battery.battery_interface import Battery
from datetime import date


class SpindlerBattery(Battery):
    """
    Represents a Spindler battery that implements the Battery interface.

    Args:
        current_date (date): The current date.
        last_service_date (date): The date when the battery was last serviced.
    """
    SERVICE_LIMIT_DAYS = 365 * 2

    def __init__(self, current_date: date, last_service_date: date):
        """
        Initialize a SpindlerBattery object.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the battery was last
                serviced.
        """
        self.current_date: date = current_date
        self.last_service_date: date = last_service_date

    def needs_service(self) -> bool:
        """
        Determines if the Spindler battery needs servicing.

        Returns:
            bool: True if the battery needs servicing, False otherwise.
        """
        return ((self.current_date - self.last_service_date).days >
                SpindlerBattery.SERVICE_LIMIT_DAYS)
