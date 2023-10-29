from tires.tires_interface import Tires
from typing import List


class OctoprimeTires(Tires):
    """
    Represents a Octoprime tires that implements the Tires interface.

    Args:
        tires (List[float]): List of tires wear.
    """

    def __init__(self, tires: List[float]) -> None:
        """
        Initialize a OctoprimeTires object.

        Args:
            tires (List[float]): List of tires wear.
        """
        self.tires:List[float] = tires

    def needs_service(self) -> bool:
        """
        Determines if the octoprime tires needs servicing.

        Returns:
            bool: True if the octoprime tires needs servicing, False otherwise.
        """
        return sum(self.tires) >= 3
