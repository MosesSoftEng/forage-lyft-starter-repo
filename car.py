from serviceable_interface import Serviceable


class Car(Serviceable):
    """Represents a car object that can be serviced."""

    def __init__(self, engine, battery):
        """
        Initialize a Car object.

        Args:
            engine: The engine of the car.
            battery: The battery of the car.
        """
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        """
        Determines if the car needs servicing.

        Returns:
            bool: True if the car needs servicing, False otherwise.
        """
        pass
