from batteries.battery_interface import Battery
from datetime import date


class NubbinBattery(Battery):
    """
    Represents a Nubbin battery that implements the Battery interface.

    This class provides a concrete implementation of a Nubbin battery, adhering to the Battery interface.

    Attributes:
        SERVICE_LIMIT_DAYS (int): The maximum number of days before the battery needs servicing.
        current_date (date): The current date.
        last_service_date (date): The date when the battery was last serviced.

    Methods:
        __init__(current_date, last_service_date): Initialize a NubbinBattery object.
        needs_service() -> bool: Determine if the Nubbin battery needs servicing.

    Usage:
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        if nubbin_battery.needs_service():
            print("The Nubbin battery needs servicing.")
        else:
            print("The Nubbin battery does not need servicing.")
    """
    SERVICE_LIMIT_DAYS = 365 * 4

    def __init__(self, current_date: date, last_service_date: date):
        """
        Initialize a NubbinBattery object.

        Args:
            current_date (date): The current date.
            last_service_date (date): The date when the battery was last
                serviced.
        """
        self.current_date: date = current_date
        self.last_service_date: date = last_service_date

    def needs_service(self) -> bool:
        """
        Determines if the Nubbin battery needs servicing.

        Returns:
            bool: True if the battery needs servicing, False otherwise.
        """
        return ((self.current_date - self.last_service_date).days >
                NubbinBattery.SERVICE_LIMIT_DAYS)
