from abc import ABC, abstractmethod


class Serviceable(ABC):
    """An abstract base class representing a serviceable item."""

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if the item needs servicing.

        Returns:
            bool: True if the item needs servicing, False otherwise.
        """
        pass
