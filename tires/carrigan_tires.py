from typing import List

from tires.tires_interface import Tires


class CarriganTires(Tires):
    """
    Represents a Carrigan tires that implements the Tires interface.

    This class provides a concrete implementation of the Tires interface for Carrigan tires.
    It contains an attribute for the list of tire wear values and a method to determine if the tires need servicing.

    Attributes:
        tires (List[float]): A list of tire wear values representing the wear levels of each tire.

    Methods:
        needs_service(): Determines if the Carrigan tires need servicing.

    Usage:
        tires = CarriganTires([0.0, 0.1, 0.9, 0.5])
        if tires.needs_service():
            print("The Carrigan tires need servicing.")
        else:
            print("The Carrigan tires do not need servicing.")
    """

    def __init__(self, tires: List[float]) -> None:
        """
        Initialize a CarriganTires object.

        Args:
            tires (List[float]): List of tires wear.
        """
        self.tires: List[float] = tires

    def needs_service(self) -> bool:
        """
        Determines if the Carrigan tires need servicing.

        Returns:
            bool: True if the Carrigan tires need servicing, False otherwise.
        """
        return any(wear >= 0.9 for wear in self.tires)
