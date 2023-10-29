from typing import List

from tires.tires_interface import Tires


class OctoprimeTires(Tires):
    """
    Represents a Octoprime tires that implements the Tires interface.

    Args:
        tires_wear (List[float]): List of tires wear.
    """

    def __init__(self, tires_wear: List[float]) -> None:
        """
        Initialize a OctoprimeTires object.

        Args:
            tires (List[float]): List of tires wear.
        """
        self.tires_wear: List[float] = tires_wear

    def needs_service(self) -> bool:
        """
        Determines if the octoprime tires needs servicing.

        Returns:
            bool: True if the octoprime tires needs servicing, False otherwise.
        """
        return sum(self.tires_wear) >= 3
