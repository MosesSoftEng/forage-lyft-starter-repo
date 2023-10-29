from abc import ABC, abstractmethod


class Battery(ABC):
    """
    Abstract base class representing a battery.
    
    This class provides a blueprint for creating battery objects. It defines an abstract method
    for determining if the battery needs servicing.
    """

    @abstractmethod
    def needs_service(self) -> bool:
        """
        Determines if the battery needs servicing.

        Returns:
            bool: True if the battery needs servicing, False otherwise.
        """
        pass
