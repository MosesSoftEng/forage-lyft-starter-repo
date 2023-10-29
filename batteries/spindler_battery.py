from batteries.battery_interface import Battery
from datetime import date


class SpindlerBattery(Battery):
    """
    Represents a Spindler battery that implements the Battery interface.

    This class provides a concrete implementation of a Spindler battery, adhering to the Battery interface.

    Attributes:
        SERVICE_LIMIT_DAYS (int): The maximum number of days before the battery needs servicing.
        current_date (date): The current date.
        last_service_date (date): The date when the battery was last serviced.

    Methods:
        __init__(current_date, last_service_date): Initialize a SpindlerBattery object.
        needs_service() -> bool: Determine if the spindler_battery battery needs servicing.

    Usage:
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        if spindler_battery.needs_service():
            print("The Spindler battery needs servicing.")
        else:
            print("The Spindler battery does not need servicing.")
    """
    SERVICE_LIMIT_DAYS = 365 * 3

    def __init__(self, current_date: date, last_service_date: date) -> None:
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
