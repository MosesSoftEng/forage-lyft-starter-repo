
from serviceable_interface import Serviceable
from engines.engine_interface import Engine
from batteries.battery_interface import Battery
from tires.tires_interface import Tires


from typing import List

class Car(Serviceable):
    """
    Represents a car object that can be serviced.

    This class provides a blueprint for creating car objects with an engine, battery, and tires.
    It implements the Serviceable interface, allowing it to be checked for servicing needs.

    Attributes:
        engine (Engine): The engine of the car.
        battery (Battery): The battery of the car.
        tires (Tires): The tires of the car.

    Methods:
        needs_service(): Determines if the car needs servicing.

    Usage:
        car = Car(engine, battery, tires)
        if car.needs_service():
            print("The car needs servicing.")
        else:
            print("The car does not need servicing.")
    """

    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        """
        Initialize a Car object.

        Args:
            engine (Engine): The engine of the car.
            battery (Battery): The battery of the car.
            tires (Tires): The tires of the car.
        """
        self.engine: Engine = engine
        self.battery: Battery = battery
        self.tires: Tires = tires

    def needs_service(self) -> bool:
        """
        Determines if the car needs servicing.

        Returns:
            bool: True if the car needs servicing, False otherwise.
        """
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
