from abc import ABC, abstractmethod


class Tires(ABC):
    """Abstract base class representing car tires."""

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if the car tires needs servicing.

        Returns:
            bool: True if the car tires needs servicing, False otherwise.
        """
        pass
