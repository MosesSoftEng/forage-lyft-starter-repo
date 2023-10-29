from tires.tires_interface import Tires
from typing import List


class CarriganTires(Tires):
    """
    Represents a Carrigan tires that implements the Tires interface.

    Args:
        current_date (date): The current date.
        last_service_date (date): The date when the battery was last serviced.
    """

    def __init__(self, tires: List[float]) -> None:
        """
        Initialize a CarriganTires object.

        Args:
            tires (List[float]): List of tires wear.
        """
        self.tires:List[float] = tires

    def needs_service(self) -> bool:
        """
        Determines if the carrigan tires needs servicing.

        Returns:
            bool: True if the carrigan tires needs servicing, False otherwise.
        """
        return any(wear >= 0.9 for wear in self.tires)
